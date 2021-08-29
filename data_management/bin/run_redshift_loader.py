from data_management.clients import redshiftClient
import yaml
from utils.constants import *



raw_conf = open("data_management/conf/data_management.yml").read()
raw_conf = raw_conf.replace("\t", " "* 8)
yaml_conf = yaml.load(raw_conf, Loader=yaml.FullLoader)


try:
    rs_section = yaml_conf[REDSHIFT]
    rs_user_name = rs_section[USERNAME]
    rs_pass_word = rs_section[USERNAME]
    rs_host = rs_section[HOST]

    rs_client = redshiftClient(rs_host, rs_user_name, rs_pass_word)

except Exception as e:
    print("Error with exception {}".format(e))