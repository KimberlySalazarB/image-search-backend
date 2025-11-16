import psycopg2
import os

DB_HOST = os.getenv("NEON_HOST")
DB_USER = os.getenv("NEON_USER")
DB_PASS = os.getenv("NEON_PASS")
DB_NAME = os.getenv("NEON_DB", "neondb")

conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port=5432,
)
conn.autocommit = True

def query_db(sql, params):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchall()
