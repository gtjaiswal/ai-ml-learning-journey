import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5433,
            database="al_ml_learning_db",
            user="al_ml_learning_user",
            password="al_ml_learning_password"
        )
        print("✅ PostgreSQL connection successful!")

        # Test query
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print(f"PostgreSQL version: {version[0]}")

        cur.close()
        conn.close()

    except OperationalError as e:
        print(f"❌ Connection failed: {e}")


if __name__ == "__main__":
    test_connection()