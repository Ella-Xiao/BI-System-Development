from data_collection import mysql_exporter_client
from utils.constants import *
import os
import traceback
import yaml

# https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.Python.html#UsingWithRDS.IAMDBAuth.Connecting.Python.AuthToken.Connect
# https://blog.panoply.io/how-to-move-your-mysql-to-amazon-redshift


raw_conf = open("data_management/conf/data_management_BOU.yml").read()
raw_conf = raw_conf.replace("\t", " " * 8)
yaml_conf = yaml.load(raw_conf, Loader=yaml.FullLoader)

try:
    mysql_section = yaml_conf[MYSQL]
    mysql_database = mysql_section[DATABASE]
    mysql_user_name = mysql_section[USERNAME]
    mysql_password = mysql_section[PASSWORD]
    mysql_host = mysql_section[HOST]
    mysql_port = mysql_section[PORT]
    query_section = mysql_section[QUERIES]
    mysql_client = mysql_exporter_client.MySQLExporter(host=mysql_host
                                                       , user=mysql_user_name
                                                       , password=mysql_password
                                                       , port=mysql_port
                                                       , database=mysql_database)

    daily_mood_query = query_section["export_daily_moods_query"]
    current_path = os.getcwd()
    mysql_client.export_query_result(daily_mood_query,
                                     "{0}/export_output/daily_moods.csv".format(current_path), True)

except Exception as e:
    print("Error with exception {}".format(e))
    traceback.print_exc()
