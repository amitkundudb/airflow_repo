from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2021, 1, 1)
}

def collecting():
    print('collecting from target DAG')

with DAG('target_dag_task',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False) as dag:

    collect_data = BashOperator(
        task_id='collect_data',
        bash_command='sleep 1'
    )

    etl_process = PythonOperator(
        task_id='etl_process',
        python_callable=collecting
    )
    collect_data >> etl_process