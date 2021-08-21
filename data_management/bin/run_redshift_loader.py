from data_management import redshift_loader_client
from utils.constants import *
import yaml




raw_conf = open("data_management/conf/data_management.yml").read()
raw_conf = raw_conf.replace("\t", " "* 8)
yaml_conf = yaml.load(raw_conf)


try:
    rs_section = yaml_conf[REDSHIFT]
    rs_user_name = rs_section[USERNAME]
    rs_pass_word = rs_section[USERNAME]
    rs_host = rs_section[HOST]

    rs_client = redshift_loader_client(rs_host, rs_user_name, rs_pass_word)

except Exception as e:
    print("Error with exception {}".format(e))