# etl_redshift_project

Goal of the Project
-> Get the data set (10000 rows) from public api
-> Load the raw data into AWS Redshift table
-> pull the desired columns from redshift to process
-> Transform the data using pandas/numpy
-> Load the transformed data into MySQL
-> Set up AWS RDS

Bonus:  Automating the Pipeline using CRON to run midnight (2 am) everyday
        Uses Flask Migrate/Alembic for database migrations

->  SQL queries, SQLAlchemy, pandas

Flask-Migrate/Alembic commands
-> Create migrations folder
flask db init
-> Create version file for migration
flask db migrate
-> Upgrade to the next version
flask db upgrade
-> Downgrade to the previous version
flask db downgrade


Cover 

Data Analysis
-> correct data types

-> duplicate rows 
df.duplicated.sum()

-> handle missing values

-> data may multiple version of same name ['Pennsylvania', 'PA', 'Penn'...]

SQL
-> Column Properties in sql tables

-> update/store processed data across multiple sql tables

-> commit/rollback sessions