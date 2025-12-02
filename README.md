# Car-Price-Prediction
This project focuses on building a machine learning model that accurately predicts the selling price of used cars based on multiple vehicle attributes. The dataset includes key features such as car age, present price, kilometers driven, fuel type, transmission, seller type, and ownership details. Extensive data preprocessing, exploratory data analysis (EDA), feature engineering, and model evaluation were performed to understand market pricing trends and build an efficient predictive system.

Multiple machine learning algorithms were trained and compared—Linear Regression, KNN, Decision Tree, Random Forest, XGBoost, and Artificial Neural Network (ANN). After evaluating all models, the ANN model achieved the highest performance with an **R² score of 0.9622**, making it the most accurate for deployment.

The final model was integrated into an interactive Streamlit web application, allowing users to input car details and obtain real-time predicted prices.

## Key Features

* End-to-end data cleaning, encoding, transformation, and outlier handling (IQR method).
* Detailed EDA: price trends, feature impact analysis, correlation study, and visualization.
* Feature engineering: car age, transformed mileage, categorical encoding, and normalization.
* Model training using multiple regression algorithms and performance comparison.
* Hyperparameter tuning to optimize model accuracy.
* Deployment-ready Streamlit app for real-time predictions.
* ANN model identified as the best performer with R² = 0.9622.

## Technologies Used

* Python, Pandas, NumPy
* Scikit-learn, XGBoost, TensorFlow/Keras
* Matplotlib, Seaborn

Streamlit

## Outcome

A highly accurate car price prediction model capable of estimating used car prices with strong reliability, suitable for real-world applications such as car dealerships, resale platforms, and valuation tools.
