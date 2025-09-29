from datetime import datetime
import requests

def log_crm_heartbeat():
    timestamp = datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    try:
        response = requests.post("http://localhost:8000/graphql", json={'query': '{ hello }'})
        if response.status_code == 200:
            status = "CRM is alive"
        else:
            status = "CRM heartbeat failed"
    except:
        status = "CRM heartbeat failed"
    
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{timestamp} {status}\n")
