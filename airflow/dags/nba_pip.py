from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import sys

# Add your local module path inside the container

from nba_data import run as extract_load_nba

with DAG(
    dag_id="nba_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",       # Updated for Airflow 2.5+
    catchup=False,
    tags=["nba", "etl", "dbt"],
) as dag:

    extract_load = PythonOperator(
        task_id="extract_load_nba",
        python_callable=extract_load_nba,
    )

    dbt_run = BashOperator(
    task_id="dbt_run",
    cwd="/opt/airflow/dags/dbt/nba_project",
    bash_command="dbt run",
)




    extract_load >> dbt_run

