# AlmaBetter Machine Learning Projects

## About the Project

This repository contains machine learning projects completed as part of my AlmaBetter program. The projects cover regression, classification, and recommendation systems, with a focus on data preprocessing, model building, evaluation, and practical applications.

## 1. Flight Price Prediction

**Objective:** Predict flight prices using historical flight data and relevant travel features.

**Work Done**
- Performed data cleaning, preprocessing, and exploratory data analysis.
- Trained and compared Linear Regression, Random Forest, and XGBoost regression models.
- Created a pipeline combining preprocessing and prediction.
- Used MLflow for experiment tracking and Flask to serve predictions through an API.

**Best Model:** Random Forest Regressor

Random Forest was selected as the final model after comparing the regression algorithms. The trained pipeline was saved as `flight_price_pipeline.pkl`.

## 2. Gender Classification

**Objective:** Predict gender categories using the available user data.

**Work Done**
- Explored the dataset and checked for missing values.
- Used `company` and `age` as input features, with `gender` as the target.
- Trained and compared Logistic Regression, Decision Tree, and Random Forest classifiers.
- Used GridSearchCV with five-fold cross-validation to tune Logistic Regression.

**Best Model:** Logistic Regression

Logistic Regression achieved approximately **38.06% test accuracy**. The dataset contained three classes: `male`, `female`, and `none`. The results indicate that predicting these categories from the selected features is challenging.

## 3. Hotel Recommendation System

**Objective:** Recommend hotels based on the user's selected destination and budget.

**Work Done**
- Explored historical travel data containing users, hotels, destinations, prices, stay duration, and travel dates.
- Analyzed popular hotels, frequently visited destinations, stay durations, and hotel prices.
- Developed a recommendation function using destination, budget, and historical hotel popularity.
- Created a Streamlit interface for users to select a destination and budget and view recommendations.

**Recommendation Approach:** Popularity-based hotel recommendation with destination and budget filtering.

The system ranks matching hotels by the frequency of their historical records. The recommendations reflect historical popularity and do not directly measure hotel quality or customer satisfaction.

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- XGBoost
- MLflow
- Flask
- Streamlit
- Matplotlib and Seaborn

## Conclusion

These projects provided practical experience in regression, classification, and recommendation systems. Through this work, I gained experience in data analysis, feature preprocessing, model comparison, hyperparameter tuning, experiment tracking, and building applications around machine learning models.
