from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def task1_function():
    print("Task 1 running")

def task2_function():
    print("Task 2 running")

def task3_function():
    print("Task 3 running")

with DAG('task_5',
         start_date=datetime(2024, 5, 1),
         schedule_interval='@daily'
         ) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=task1_function,
        retries=2,
        retry_delay=timedelta(minutes=5)
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=task2_function
    )

    task3 = PythonOperator(
        task_id='task3',
        python_callable=task3_function
    )

    task1 >> task2 >> task3