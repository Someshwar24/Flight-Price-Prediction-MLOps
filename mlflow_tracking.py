import joblib
import mlflow

mlflow.set_experiment("Flight price prediction")

model = joblib.load("flight_price_model.pkl")

with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)

    mlflow.log_metric("mae", 0.0405)
    mlflow.log_metric("rmse", 0.6212)
    mlflow.log_metric("r2", 0.999997)

    #mlflow.sklearn.log_model(sk_model = model,name= "random_forest_model")
    mlflow.log_artifact("flight_price_model.pkl")

    print("MLflow run completed successfully!")