from flask import request, Blueprint, jsonify

from ..utils.redshift_connection import redshift_connection

api_blueprint = Blueprint('api', __name__)

database_name = 'dev'
workgroup_name = 'default-workgroup'
# sql_statement = 'CREATE TABLE '+'city_data'+' (city integer, task_data varbinary);'
sql_statement = 'DELETE TABLE city_data;'

@api_blueprint.route('/health', methods=['GET'])
def check_app_health():
    conn = redshift_connection()

    response = conn.execute_statement(
        Database=database_name,
        WorkgroupName=workgroup_name,
        Sql=sql_statement
    )
    
    print(f"Create Table sql statement executed: {response}")

    return jsonify(message='ETL Project!!')
