from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow_flight_workflow import validate_flight_data
from airflow_log_mlflow import log_training_results
from airflow_train_flight_model import train_flight_model

with DAG(
    dag_id="flight_price_workflow",
    start_date=datetime(2026, 10, 9),
    schedule=None,
    catchup=False,
    tags=["flight-price", "mlops"],
) as dag:

    validate_data = PythonOperator(
        task_id="validate_flight_data",
        python_callable=validate_flight_data,
    )

    train_model = PythonOperator(
        task_id="train_flight_model",
        python_callable=train_flight_model,
    )

    log_results = PythonOperator(
        task_id="log_mlflow_results",
        python_callable=log_training_results,
    )

    validate_data >> train_model >> log_results
