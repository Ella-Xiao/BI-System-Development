# from __future__ import absolute_import
# import sys
# sys.path.append("/Users/demonxy468/git/health-analytics-system")
from utils.constants import *
import yaml
import os
from data_management.clients.s3Client import S3Client

dirname = os.path.dirname(__file__)
filename_path = os.path.join(dirname, '../conf/')

print("Hello World!")
print("Running the code: run_redshift_loader.py")

raw_conf = open(filename_path + 'data_management.yml').read()
raw_conf = raw_conf.replace("\t", " " * 8)
yaml_conf = yaml.load(raw_conf, Loader=yaml.FullLoader)

aws_section = yaml_conf[AWS]
aws_access_key = open(filename_path + aws_section[ACCESS_KEY]).read().strip()
aws_secret_key = open(filename_path + aws_section[SECRET_KEY]).read().strip()

s3 = S3Client(aws_access_key, aws_secret_key)

print(s3.listBucket())

