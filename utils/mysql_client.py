import pyodbc
import logging
import time


class MySQLClient:
    def __init__(self, host, port, user, password, database, driver="MySQL", max_retries=3, sleep_interval=60):
        self.params = vars()
        self.max_retries = max_retries
        self.sleep_interval = sleep_interval
        self.init_connection()

    def init_connection(self):
        dsn = "DRIVER={MySQL ODBC 3.51 Driver}; SERVER=localhost;DATABASE=mydb; UID=root; PASSWORD=thatwouldbetelling;"
        tries = 0
        while tries < self.max_retries:
            try:
                self.connection = pyodbc.connect(dsn)
            except Exception as e:
                logging.warning("MySQL Connection Failed: '%s'" % str(e))
                time.sleep(self.sleep_interval)
                tries += 1
        raise Exception("Unable to acquire MySQL connection after %s tries" % tries)

    def get_connection(self):
        if self.connection:
            return self.connection
        self.init_connection()
        return self.connection

    def close_connection(self):
        if self.connection:
            logging.info("Closing Connection...")
            try:
                self.connection.close()
            except Exception as e:
                logging.warning("Failed to close MySQL Connection: '%s'" % str(e))
            self.connection = None

    def select(self, query):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
