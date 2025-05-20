import boto3
import psycopg2
import logging
import os
from dotenv import load_dotenv
# import ConfigParser

load_dotenv()

def redshift_connection():
    logger = logging.getLogger(__name__)
    # parser = ConfigParser.ConfigParser()
    # parser.read('config.ini')
    print("Establishing Redshift connection !!")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    client = boto3.client('redshift-data', 
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name='us-west-2'
                        )
    # sqlstmt = 'CREATE TABLE '+'batch_processing_tasks'+' (task_id integer, task_data varbinary);'
    # response = client.execute_statement(
    #     Database='dev',
    #     WorkgroupName="dev-workgroup",
    #     Sql=sqlstmt
    # )
    
    # print(f"sql_statement response create table {response}")

    # print("Connection Established with AWS Redshift redshift_data_client!")
    # sql_statement = "SELECT * FROM batch_processing.tasks"
    # response = client.execute_statement(
    #     Database='dev',
    #     WorkgroupName="dev-workgroup",
    #     Sql=sql_statement
    # )
    # print(f"sql_statement response  {response}")
    # cluster_creds = client.get_credentials(dbName="dev",
    #                                         durationSeconds=1200,
    #                                         workgroupName="dev-workgroup")

    # print(f"Cluster Credentials {cluster_creds}")

    # response = client.get_workgroup(
    # workgroupName='dev-workgroup'
    # )
    # print(f"Workgroup response  {response}")
    # try:
    # conn = psycopg2.connect(
    #     host="dev-workgroup.979907616055.us-east-1.redshift-serverless.amazonaws.com",
    #     port="5439",
    #     user=cluster_creds["dbUser"],
    #     password=cluster_creds['dbPassword'],
    #     database="dev"
    # )
    # print(f"connnnnnecttttttt {conn}")
    # conn = redshift_connector.connect(
    #     # host="dev-workgroup.979907616055.us-east-1.redshift-serverless.amazonaws.com",
    #     # port="5439",
    #     # user=cluster_creds["dbUser"],
    #     # password=cluster_creds['dbPassword'],
    #     # database="dev",
        # iam=True,
        # host='default-workgroup.979907616055.us-east-1.redshift-serverless.amazonaws.com',
        # database='dev',
        # access_key_id=aws_access_key_id,
        # secret_access_key=aws_secret_access_key,
    # )
    print(f"Cluster Connection Established {client}")
    return client
    # except psycopg2.Error:
    #     logger.exception('Failed to open database connection.')
    #     print("Failed to connect with Redshift cluster")



def authenticate_weatherstack():
    WEATHER_STACK_KEY = os.getenv("weatherstack_api_key")
    external_url = f'http://api.weatherstack.com/current?access_key={WEATHER_STACK_KEY}&query=London;'
    return external_url