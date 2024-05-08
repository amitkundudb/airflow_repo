from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'amitdb',
    'start_date': datetime(2024, 2, 7),
    'retries': 1,
    'retry_delay': timedelta(seconds=1)
}
def greet(ti):
    first_name = ti.xcom_pull(task_ids = 'get_name',key = 'first_name')
    last_name = ti.xcom_pull(task_ids = 'get_name',key = 'last_name')
    age = ti.xcom_pull(task_ids = 'get_age',key = 'age')
    print(f"My name is {first_name} {last_name} and age is {age}")

def get_name(ti):
    ti.xcom_push(key = 'first_name',value = 'Amit')
    ti.xcom_push(key = 'last_name',value = 'Kundu')
def get_age(ti):
    ti.xcom_push(key = 'age',value = 23)

with DAG(
    'task_3',
    default_args=default_args,
    description='DAG with PythonOperator',
    schedule_interval='@monthly'
) as dag:
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable = greet
    )
    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable = get_name
    )
    task3 = PythonOperator(
        task_id = 'get_age',
        python_callable= get_age
    )
    [task2,task3] >> task1