import logging
import mysql.connector
import csv


class MySQLExporter:
    def __init__(self, host, user, password, port=3306, database=None, delimiter=None):
        self.host = host,
        self.user = user,
        self.password = password,
        self.port = port,
        self.database = database,
        self.delimiter = delimiter
        self.connection = self.initiate_connection()

    def initiate_connection(self):
        connection = mysql.connector.connect(host=self.host[0],
                                             user=self.user[0],
                                             passwd=self.password[0],
                                             port=self.port[0],
                                             database=self.database[0])
        return connection

    def export_query_result(self, query, filename, do_gzip=True):
        cursor = self.connection.cursor()
        cursor.execute(query)
        query_results = cursor.fetchall()
        headers = [i[0] for i in cursor.description]
        print(query_results)
        cursor.close()
        num_rows = self.dump_to_file(query_results, headers, filename, do_gzip)
        return num_rows

    def dump_to_file(self, rows, headers, filename):
        logging.info("dumping data into csv file")
        csv_file = open(filename, 'w')
        if rows:
            myFile = csv.writer(csv_file)
            myFile.writerow(headers)
            myFile.writerows(rows)
