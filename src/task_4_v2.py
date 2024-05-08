from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2021, 1, 1)
}
def triggering():
    print('triggering')

with DAG('trigger_dag_task',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False) as dag:

    triggering = PythonOperator(
        task_id='triggering',
        python_callable= triggering
    )
    trigger_target = TriggerDagRunOperator(
        task_id = 'trigger_target',
        trigger_dag_id= 'target_dag_task'
    )