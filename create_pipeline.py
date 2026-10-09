import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


df = pd.read_csv("flights.csv")

if "date" not in df.columns or "price" not in df.columns:
    raise ValueError("The dataset must contain 'date' and 'price' columns.")

df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y", errors="coerce")
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

feature_frame = df.drop(columns=["price", "date", "travelCode", "userCode"], errors="ignore")
target = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    feature_frame, target, test_size=0.2, random_state=42
)

numerical_cols = feature_frame.select_dtypes(include="number").columns.tolist()
categorical_cols = feature_frame.select_dtypes(exclude="number").columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ],
    remainder="drop",
)

model = RandomForestRegressor(n_estimators=200, random_state=42)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model),
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "flight_price_pipeline.pkl")
loaded_pipeline = joblib.load("flight_price_pipeline.pkl")

sample_input = X_test.iloc[[0]]

prediction = loaded_pipeline.predict(sample_input)

print("Predicted Flight Price:", prediction[0])
print("Actual Flight Price:", y_test.iloc[0])
print("Deployment pipeline created successfully")

