from airflow.models import DAG
from airflow.sensors.filesystem import FileSensor

from datetime import datetime

default_args = {
    'owner':'amitdb',
    'start_date' : datetime(2024, 5, 1),

}

with DAG (dag_id='file_sensor',
          schedule_interval='@daily',
          default_args=default_args,
          catchup = False) as dag:
    sensing_task = FileSensor(
        task_id = 'wait_for_file',
        poke_interval=30,
        # EVERY 30 SECONDS IT WILL CHECK FOR FILE EXISTANCE
        timeout=60 * 5,
        # It will stop checking after 5 min, It will always better to use timeout to avoid deadlock
        mode = 'reschedule',
        filepath='revised_detailed_topics.docx',
        fs_conn_id='file_system'
    )