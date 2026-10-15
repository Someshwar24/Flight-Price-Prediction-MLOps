
import pandas as pd
import streamlit as st

df = pd.read_csv("hotels.csv")

def recommend_hotels(destination, budget, top_n=5):
    hotels = df[
        (df["place"].str.lower() == destination.lower()) &
        (df["price"] <= budget)
    ]

    return (
        hotels.groupby("name")
        .agg(
            Average_Price=("price", "mean"),
            Popularity=("name", "count")
        )
        .sort_values("Popularity", ascending=False)
        .head(top_n)
        .reset_index()
    )

st.title("Hotel Recommendation System")
st.write("Find hotels based on destination and budget.")

destination = st.selectbox(
    "Choose a destination",
    sorted(df["place"].dropna().unique())
)

budget = st.number_input(
    "Maximum daily price",
    min_value=0.0,
    value=300.0
)

if st.button("Recommend Hotels"):
    result = recommend_hotels(destination, budget)

    if result.empty:
        st.warning("No hotels found. Try increasing your budget.")
    else:
        st.dataframe(result, use_container_width=True)
