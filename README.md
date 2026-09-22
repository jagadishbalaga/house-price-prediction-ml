# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts the price of a house based on different features such as living area, number of bedrooms, bathrooms, house grade, location, condition, and other property-related information.

The main goal of this project is to understand and implement a complete Machine Learning workflow, starting from data analysis and preprocessing to model training, evaluation, tuning, and deployment.

---

## 📊 Dataset

The dataset contains **14,619 house records** with information about different properties.

Some important features include:

- Number of bedrooms
- Number of bathrooms
- Living area
- Lot area
- Number of floors
- Waterfront
- Number of views
- House condition
- House grade
- Basement area
- Built year
- Renovation year
- Latitude and Longitude
- Number of schools nearby
- Distance from airport

### Target Variable

`Price`

The model uses the other house features to predict the house price.

---

## 🔍 Data Analysis

First, I explored the dataset to understand its structure and quality.

The following steps were performed:

- Checked dataset shape and columns
- Checked data types
- Checked missing values
- Checked duplicate records
- Checked unique values
- Analyzed statistical summary
- Studied correlations between features and house price
- Identified potential outliers in house prices

The analysis showed that features such as **living area, house grade, house area, and number of bathrooms** have a strong relationship with house price.

---

## 🛠️ Feature Engineering

Some preprocessing and feature engineering steps were performed before training the models.

- Removed `id` because it is an identifier rather than a useful predictive feature.
- Converted the Excel-style `Date` column into a proper date format.
- Extracted `Year` and `Month` from the date.
- Removed the original `Date` column after extracting the required information.
- Separated the features (`X`) and target (`y`).

---

## 🤖 Machine Learning Models

I trained and compared multiple regression models:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Tuned Random Forest Regressor

The models were evaluated using:

- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**
- **R² Score**

For MAE and RMSE, lower values indicate smaller prediction errors.

For R², a higher value indicates that the model explains more of the variation in the target variable.

---

## ⚙️ Hyperparameter Tuning

After training the Random Forest model, I used **GridSearchCV** to find better hyperparameter combinations.

The tuning process tested parameters such as:

- Number of trees
- Maximum tree depth
- Minimum samples required for splitting
- Minimum samples required at a leaf

The tuned model was then evaluated on the test dataset.

---

## 💾 Model Saving

After training, the final model was saved using `joblib`.

```python
joblib.dump(best_rf_model, 'house_price_model.pkl')

🌐 Streamlit Deployment

The trained model is connected to a Streamlit web application.

The application allows a user to enter house details and receive a predicted house price.
To run the application:
python -m streamlit run apps.py
