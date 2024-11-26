from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.scrape_data import fetcher
from src.preprocessing import preprocess

args = {
    "start_date": datetime(2024, 10, 10),
    "retries": 3,
    "email": ["talhanadeem185185@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": False,
}

with DAG("class_act_7_pipeline", default_args=args, schedule_interval="@hourly", description="Fetching and Preprocessing data",) as dag:
    collect_data_1 = PythonOperator(
        task_id="collect_data",
        python_callable=fetcher,
    )

    preprocess_data_2 = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess,
    )

    collect_data_1 >> preprocess_data_2


