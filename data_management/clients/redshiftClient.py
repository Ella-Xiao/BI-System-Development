import boto3
import yaml
import psycopg2
import logging


class redshiftLoaderClient:
    def __init__(self, host, username, password, access_key, secret_key, dbname, port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.access_key = access_key
        self.secret_key = secret_key
        self.port = port
        self.dbname = dbname,
        self.host = host,
        self.port = port,
        self.user = username,
        self.password = password,
        self.connection = self.initiate_connection()

    def initiate_connection(self):
        connection = psycopg2.connect(dbname=self.dbname, host=self.host,
                                      port=self.port, user=self.username, password=self.password)
        return connection

    def get_connection(self):
        if not self.connection:
            self.connection = self.initiate_connection()

    def close_connection(self):
        if self.connection:
            logging.info("closing connection")
            try:
                self.connection.close()
            except Exception as e:
                logging.error(e)
            self.connection = None

    # Redshift to S3
    def unload_data(self, table, s3_path):

        unload_sql = """
        unload ('select * from {table}')
        to '{s3_path}' credentials 
        'aws_access_key_id={access_key};aws_secret_access_key={secret_key}'
        parallel off;
        """.format(table, s3_path, self.access_key, self.secret_key)
        try:
            cur = self.connection.cursor()
            cur.execute(unload_sql)
            cur.close()
        except Exception as e:
            logging.error(e)
        return 0

    # S3 to Redshift
    def copy_data(self, table, s3_path):
        copy_sql = """
        copy {table}
        from '{s3_path}'
        access_key_id '<access-key-id>'
        secret_access_key {access_key}
        session_token {secret_key}; 
        """.format(table, s3_path, self.access_key, self.secret_key)
        try:
            cur = self.connection.cursor()
            cur.execute(copy_sql)
            cur.close()
        except Exception as e:
            logging.error(e)
        return 0

    # Run any SQL statements
    def execute(self, query, select=False):
        try:
            cur = self.connection.cursor()
            cur.execute(query)
            row_count = cur.rowcount()
            logging.info("row_count = {row_count}".format(row_count))
            if select:
                results = []
                rows = cur.fetchall()
                for row in rows:
                    results.append(row)
                cur.close()
                return results
            else:
                cur.close()
                return row_count
        except Exception as e:
            logging.error(e)
        return 0
