from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'Amit',
    'start_date':datetime(2024, 5, 5, 2),
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="simple_dag",
    default_args=default_args,
    description="This is a simple DAG with BashOperator and schedule_interval",
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task'
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hello world, this is the second task dependent on task1'
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hello world, this is the third task dependent on task1'
    )
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    task1 >> [task2,task3]