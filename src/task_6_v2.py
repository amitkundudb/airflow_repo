from airflow import DAG
from airflow.sensors.http_sensor import HttpSensor
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=1),
}

dag = DAG(
    'http_sensor',
    default_args=default_args,
    description='A simple example DAG with HttpSensor and PythonOperator',
    schedule_interval=timedelta(days=1),
)

def my_task():
    print("HttpSensor task completed successfully.")

http_sensor_task = HttpSensor(
    task_id='http_sensor_task',
    http_conn_id='http_sensor_connection',
    endpoint='',
    method='GET',
    dag=dag,
)

python_operator_task = PythonOperator(
    task_id='python_operator_task',
    python_callable=my_task,
    dag=dag,
)

http_sensor_task >> python_operator_task
