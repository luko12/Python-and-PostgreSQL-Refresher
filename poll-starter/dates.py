import pytz
import json
import datetime
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get("DATABASE_URI"))

user_timezone = pytz.timezone("Europe/London")

new_post_content = input("Enter what you learned today: ")

new_post_date = user_timezone.localize(datetime.datetime.now())
utc_post_date = new_post_date.astimezone(pytz.utc)

with connection:
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO posts (content, date) VALUES (%s, %s)",
                       (new_post_content, utc_post_date.timestamp()))


