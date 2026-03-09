import psycopg2
from utils.logger import get_logger
import os

logger = get_logger()

class DBClient:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.dbname = os.getenv("DB_NAME", "demoblaze_mock")
        self.user = os.getenv("DB_USER", "qa_user")
        self.password = os.getenv("DB_PASS", "qa_password")
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.dbname,
                user=self.user,
                password=self.password
            )
            logger.info("Connected to PostgreSQL successfully")
        except Exception as e:
            logger.error(f"PostgreSQL Connection Failed: {e}")

    # def execute_query(self, query, params=()):
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute(query, params)
    #         self.connection.commit()
    #         return cursor
    #     except Exception as e:
    #         self.connection.rollback()
    #         logger.error(f"Database Error: {e}")
    #         raise e

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("PostgreSQL connection closed")