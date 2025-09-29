#!/usr/bin/env python3
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime, timedelta

# GraphQL client setup
transport = RequestsHTTPTransport(url='http://localhost:8000/graphql', verify=False)
client = Client(transport=transport, fetch_schema_from_transport=True)

# GraphQL query for recent orders
query = gql("""
query {
  orders(filter: {orderDateGte: "%s"}) {
    id
    customer {
      email
    }
  }
}
""" % (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'))

result = client.execute(query)

# Log reminders
with open("/tmp/order_reminders_log.txt", "a") as f:
    for order in result['orders']:
        f.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')} - Order ID: {order['id']}, Email: {order['customer']['email']}\n")

print("Order reminders processed!")
