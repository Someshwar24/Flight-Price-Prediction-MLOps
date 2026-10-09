from flask import Flask, request, jsonify
import joblib
import pandas as pd
import mlflow

app = Flask(__name__)

model = joblib.load("flight_price_pipeline.pkl")
mlflow.set_experiment("Flight price prediction API")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flight Price Prediction API is running"})

@app.route("/predict",methods=["POST"])
def predict():
    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]

    with mlflow.start_run():
        mlflow.log_param("flight_type", data["flightType"])
        mlflow.log_param("agency", data["agency"])
        mlflow.log_metric("predicted_price", float(prediction))
    return jsonify({"predicted_price": round(float(prediction), 2)})

if __name__ == "__main__":
    app.run(debug=True)
    