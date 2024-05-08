from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'name',
    'start_date': datetime(2024, 2, 16),
    'retries': 1,
    'retry_delay': timedelta(seconds=1)
}

dag_a = DAG(
    'task_2',
    default_args=default_args,
    description='Airflow DAG with five tasks using BashOperator',
    schedule_interval='@monthly'
)

task1 = BashOperator(
    task_id='task1',
    bash_command='echo "Executing Task 1"',
    dag=dag_a
)

task2 = BashOperator(
    task_id='task2',
    bash_command='echo "Executing Task 2"',
    dag=dag_a
)

task3 = BashOperator(
    task_id='task3',
    bash_command='echo "Executing Task 3"',
    dag=dag_a
)

task4 = BashOperator(
    task_id='task4',
    bash_command='echo "Executing Task 4"',
    dag=dag_a
)

task5 = BashOperator(
    task_id='task5',
    bash_command='echo "Executing Task 5"',
    dag=dag_a
)

task1 >> task3 >> task4
task2 >> task5