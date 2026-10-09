
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


def train_flight_model():
    df = pd.read_csv("flights.csv")

    df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y", errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    X = df.drop(columns=["price", "date", "travelCode", "userCode"])
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    categorical_cols = X.select_dtypes(exclude="number").columns.tolist()

    numerical_cols = X.select_dtypes(include="number").columns.tolist()

    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), numerical_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
    ])

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(n_estimators=100,random_state=42,n_jobs=-1))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    joblib.dump(pipeline, "flight_price_pipeline.pkl")

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Flight model training completed.")
    print("MAE:", mae)
    print("R2:", r2)

    return {"mae": float(mae), "r2": float(r2)}


if __name__ == "__main__":
    train_flight_model()
