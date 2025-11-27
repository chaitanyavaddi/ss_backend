import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv('POSTGRES_URL')
 
def get_conn():
    conn = psycopg2.connect(DB_URL)
    return conn