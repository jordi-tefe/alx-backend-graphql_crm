#!/bin/bash

# Activate virtual environment
source /path/to/your/venv/bin/activate

# Run Django shell command to delete inactive customers
DELETED_COUNT=$(python /path/to/your/manage.py shell -c "
from crm.models import Customer
from django.utils import timezone
from datetime import timedelta

one_year_ago = timezone.now() - timedelta(days=365)
deleted, _ = Customer.objects.filter(orders__isnull=True, created_at__lt=one_year_ago).delete()
print(deleted)
")

# Log results with timestamp
echo \"$(date '+%d/%m/%Y-%H:%M:%S') Deleted $DELETED_COUNT inactive customers\" >> /tmp/customer_cleanup_log.txt
