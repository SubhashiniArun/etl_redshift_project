import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def redshift_connection():
    print("Establishing Redsfift connection!!")

    client = boto3.client('redshift-data',
                          aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                          region_name='us-west-2'
                          )
    print('Established Redshift connection')
    return client