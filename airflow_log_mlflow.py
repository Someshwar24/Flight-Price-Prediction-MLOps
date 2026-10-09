
import mlflow

def log_training_results(**context):
    metrics = context['task_instance'].xcom_pull(task_ids='train_flight_model')
    mlflow.set_experiment("Flight Price Prediction Airflow")

    # Start an MLflow run
    with mlflow.start_run():
        mlflow.log_param("model", "Random Forest Regressor")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)

        mlflow.log_metric("mae", metrics["mae"])
        mlflow.log_metric("r2", metrics["r2"])

        print("MLflow metrics logged successfully.")
        print("MAE:", metrics["mae"])
        print("R2:", metrics["r2"])

if __name__ == "__main__":
    log_training_results()
