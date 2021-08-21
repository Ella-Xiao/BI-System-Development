import boto3
import yaml

class redshiftLoaderClient:
    def __int__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    # Redshift to S3
    def unload_data(self):
        return 0


    # S3 to Redshift
    def copy_data(self):
        return 0



