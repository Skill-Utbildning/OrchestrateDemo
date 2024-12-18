from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


def readcsv():
    account_df = pd.read_csv("./scripts/data/account.csv")
    print(account_df.head())

with DAG(
    'readcsv',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 10, 31),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='readcsv',
        python_callable=readcsv,
    )

    task1
