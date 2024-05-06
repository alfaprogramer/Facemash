import os
import json
from django.core.management import call_command
from django.db import connection
from mash.models import Image,UserData

# Export data from SQLite to JSON file
with open('data.json', 'w') as f:
    call_command('dumpdata', 'mash', stdout=f)

# Connect to PostgreSQL database
connection.close()  # Close existing SQLite connection
os.environ["DJANGO_DB_NAME"] = "facemash_9f3p"
os.environ["DJANGO_DB_USER"] = "facemash_9f3p_user"
os.environ["DJANGO_DB_PASSWORD"] = "jDtwrMHQwgG4jlklbZl5oqmETINZLHC2"
os.environ["DJANGO_DB_HOST"] = "dpg-cosfet20si5c739utrm0-a"
os.environ["DJANGO_DB_PORT"] = "5432"

# Load data from JSON file and insert into PostgreSQL database
with open('data.json', 'r') as f:
    data = json.load(f)
    for obj in data:
        UserData.objects.create(**obj['fields'])  # For inserting into the UserData model
        # OR
        Image.objects.create(**obj['fields'])     # For inserting into the Image model