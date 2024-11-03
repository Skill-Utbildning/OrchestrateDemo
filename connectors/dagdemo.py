import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator   

import pandas as pd

def read_csv():
    df = pd.read_csv('your_csv_file.csv')
    return df

def process_data(df):
    # Apply your data processing logic here
    return df

def write_to_snowflake(df):
    # Replace with your Snowflake connection details
    snowflake_conn = {
        'user': 'your_username',
        'password': 'your_password',
        'account': 'your_account_name',
        'warehouse': 'your_warehouse_name',
        'database': 'your_database_name',
        'schema': 'your_schema_name'   

    }

    sql = "CREATE TABLE your_table (column1 VARCHAR, column2 INT)"
    snowflake_op = SnowflakeOperator(
        task_id='write_to_snowflake',
        sql=sql,
        snowflake_conn_id='your_snowflake_conn'
    )

    df.to_parquet(f'snowflake://{snowflake_conn["user"]}@{snowflake_conn["account"]}/{snowflake_conn["database"]}/{snowflake_conn["schema"]}/your_table', index=False)

    return snowflake_op

with DAG(
    'csv_to_parquet_dag',
    schedule_interval='@daily',
    default_args={'start_date': datetime.datetime(2024, 11, 4)}
) as dag:
    read_csv_task = PythonOperator(
        task_id='read_csv',
        python_callable=read_csv
    )

    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        provide_context=True
    )

    write_to_snowflake_task = PythonOperator(
        task_id='write_to_snowflake',
        python_callable=write_to_snowflake,
        provide_context=True
    )

    read_csv_task >> process_data_task >> write_to_snowflake_task