
import pandas as pd

def validate_flight_data():
    df = pd.read_csv("flights.csv")

    required_columns = [
        "travelCode",
        "userCode",
        "from",
        "to",
        "flightType",
        "price",
        "time",
        "distance",
        "agency",
        "date"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("Flight data loaded successfully!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Missing values:", int(df.isnull().sum().sum()))

if __name__ == "__main__":
    validate_flight_data()
