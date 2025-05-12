from flask import request, Blueprint, jsonify
import requests
import pandas as pd

from ..utils.redshift_connection import redshift_connection, authenticate_weatherstack

api_blueprint = Blueprint('api', __name__)

database_name = 'dev'
workgroup_name = 'default-workgroup'
create_sql_statement = 'CREATE TABLE IF NOT EXISTS '+'astro_data'+' (sunrise VARCHAR(255), sunset VARCHAR(255), moonrise VARCHAR(255), moonset VARCHAR(255), moon_phase VARCHAR(255), moon_illumination INT);'
delete_sql_statement = 'DELETE TABLE astro_data;'
# load_sql_statement = f"""INSERT INTO city_data (city, value, timestamp) VALUES ('{}', '{}', '{}')"""



def fetch_external_api_data():
    weatherstack_url = authenticate_weatherstack()
    response = requests.get(weatherstack_url)
    current_data = response.json()['current']['astro']
    print(f"current astro data {current_data}")
    df = pd.DataFrame(current_data, index=[0])
    print(f"DF {df}")
    print(df.info())
    return df

def create_redshift_table(conn):

    # Creating Redshift city_data table in Redshift
    response = conn.execute_statement(
        Database=database_name,
        WorkgroupName=workgroup_name,
        Sql=create_sql_statement
    )
    return response


def load_data_into_redshift(conn, df):
    
    for _, row in df.iterrows():
        sunrise=row['sunrise']
        sunset=row['sunset']
        moonrise=row['moonrise']
        moonset=row['moonset']
        moon_phase=row['moon_phase']
        moon_illumination=row['moon_illumination']
        load_sql_statement = f"""INSERT INTO astro_data (sunrise, sunset, moonrise, moonset, moon_phase, moon_illumination) VALUES ('{sunrise}', '{sunset}', '{moonrise}', '{moonset}', '{moon_phase}', '{moon_illumination}')"""
        conn.execute_statement(
            Database=database_name,
            WorkgroupName=workgroup_name,
            Sql=load_sql_statement
        )
    return

# def extract_from_redshift(conn):
#     extract_sql_statement = f"""SELECT * FROM astro_data"""
#     response = conn.execute_statement(
#         Database=database_name,
#         WorkgroupName=workgroup_name,
#         Sql=extract_sql_statement
#     )
#     print(f"RESPONSE extract {response}")
#     return

def transform_raw_data(df):

    return "hello"


def load_tranformed_data_into_mysql():
    return


@api_blueprint.route('/run-etl', methods=['GET'])
def run_etl():

    # Fetch the city data from external API
    df = fetch_external_api_data()


    # # Redshift connection established
    conn = redshift_connection()

    # # Create Redshift table
    response = create_redshift_table(conn)
    # print(f"Table Created response: {response}")

    # Load to Redshift
    load_data_into_redshift(conn, df)
    print("Data loaded into redshift")
    
    # Extract from Redshift
    # extracted_data = extract_from_redshift(conn)

    # Transform the raw data
    # transformed_data = transform_raw_data(extracted_data  )

    # # Load the transformed data into MySQL
    # load_tranformed_data_into_mysql(transformed_data)

    # print(f"Create City Table sql statement executed if it does not exist: {response}")

    # Load the raw data into Redshift table
    return jsonify(message='ETL Project!!')
