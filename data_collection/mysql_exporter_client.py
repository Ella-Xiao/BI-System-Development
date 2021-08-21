import re
import os
import gzip
import json
import time
import logging

class MySQLExporter:
    def __init__(self, access_key, secret_key, bucket, s3_prefix, delimiter, temp_dir, table_list, client_mysql):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket = bucket
        self.s3_prefix = s3_prefix
        self.delimiter = delimiter
        self.temp_dir = temp_dir
        self.table_list = table_list
        self.client_mysql = client_mysql


    def dump_to_file(self, rows, filename, do_gzip=True):
        num_rows = 0
        f = None
        if not do_gzip:
            f = open(filename, "wb")
        else:
            f = gzip.open(filename, "wb")
        for row in rows:
            f.write((self.delimiter.decode("string_escape").join(
                [("%s" % x).replace("\n", " ") if x is not None else "" for x in row]) + "\n").encode("utf-8"))
            num_rows += 1
        f.close()
        logging.info("wrote %d rows to %s" % (num_rows, filename))
        return num_rows