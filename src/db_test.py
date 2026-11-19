import psycopg2
from config_helper import get_db_config

conn = psycopg2.connect(**get_db_config())
try:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'market_analysis_cache';
        """)
        print("Current market_analysis_cache Columns:")
        for row in cur.fetchall():
            print(f" -> {row[0]} ({row[1]})")
finally:
    conn.close()