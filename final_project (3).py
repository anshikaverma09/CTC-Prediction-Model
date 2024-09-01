# -*- coding: utf-8 -*-
"""Final_project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18k6PdwrcqixbsR7r4WmA1LRDkiRjTaWo
"""

import pandas as pd
import numpy as np
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/Intershala_Notebook/ML case Study.csv")
college = pd.read_csv("/content/drive/MyDrive/Intershala_Notebook/Colleges.csv")
cities = pd.read_csv("/content/drive/MyDrive/Intershala_Notebook/cities.csv")

df.head()

college.head()

cities.head()

Tier1 = college["Tier 1"].tolist()
Tier2 = college["Tier 2"].tolist()
Tier3 = college["Tier 3"].tolist()

Tier1

for item in df.College:
    if item in Tier1:
        df["College"].replace(item,3,inplace=True)
    elif item in Tier2:
        df["College"].replace(item,2,inplace=True)
    elif item in Tier3:
        df["College"].replace(item,1,inplace=True)

df.head()

metro = cities['Metrio City'].tolist()
non_metro_cities = cities['non-metro cities'].tolist()

for item in df.City:
    if item in metro:
        df['City'].replace(item,1,inplace=True)
    elif item in non_metro_cities:
        df['City'].replace(item,0,inplace=True)

df.head()

df = pd.get_dummies(df, drop_first=True)

df.sample(5)

df.isna().sum()

df.info()

df.describe()

#Outlier Detection
sns.boxplot(df['Previous CTC'])

sns.boxplot(df['Graduation Marks'])

sns.boxplot(df['EXP (Month)'])

sns.boxplot(df['CTC'])

# Corelation between variables
corr = df.corr()
corr

# Visual representation of corr
# Heatmap
sns.heatmap(data=corr)

#Outlier present in previous CTC column
percent25 = df['Previous CTC'].quantile(0.25)
percent75 = df['Previous CTC'].quantile(0.75)

iqr = percent75-percent25

upper_limit = percent75 + 1.5*iqr
lower_limit = percent25 - 1.5*iqr

#In the above DataFrame, These are outliers present in "Previous CTC"column. As seen these outliers are not extreme, so in my opinion keeping these data may not affect much on my model.

#Outlier Present in CTC column
percent25 = df['CTC'].quantile(0.25)
percent75 = df['CTC'].quantile(0.75)

iqr = percent75-percent25

upper_limit = percent75 + 1.5*iqr
lower_limit = percent25 - 1.5*iqr

df[(df['CTC'] < lower_limit) | (df['CTC'] > upper_limit)]

#Conclusion on detection of Outliers:
#There were as such no extreme outliers present in our dataset that can make any huge difference in machine learning model. Also from describe function it is clear that there is no extreme outliers.
#As seen above in "Previous CTC" and "CTC", there are some outliers but from my perspective these are not going to affect my model.
#In the HeatMap figure, there are some relation between Role_manager and CTC and Previous CTC and CTC

#Applying Machine Learning models without Feature Scaling
#Here I am applying all possible algorithm without any scaling to check performance of model

# Import necessary libraries for data splitting, modeling, and evaluation

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Split data into dependent and Independent Variable

X = df.loc[:, df.columns != 'CTC']
y = df['CTC']

# Split Data into train and test with test_size = 0.2(80% data into train and 20% to test)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

y_test

# Create a LinearRegression model
linear_reg = LinearRegression()

# Fit the model to the training data
linear_reg.fit(X_train, y_train)

# Make predictions on the test data
linear_reg_pred = linear_reg.predict(X_test)

# Calculate and print the R-squared (r2) score
print("r2_score:",r2_score(y_test, linear_reg_pred))

# Calculate and print the Mean Absolute Error (MAE)
print("MAE:", mean_absolute_error(y_test, linear_reg_pred))

# Calculate and print the Mean Squared Error (MSE)
print("MSE:", mean_squared_error(y_test, linear_reg_pred))

print()

# Print the coefficients of the linear regression model
print("Coef:",linear_reg.coef_)

# Print the intercept of the linear regression model
print("Intercept:",linear_reg.intercept_)

# Import the Ridge regression model
ridge = Ridge()

# Fit the model to training data
ridge.fit(X_train, y_train)

# Make prediction on test data
ridge_predict = ridge.predict(X_test)

# Calculate and print the R-squared (r2) score
print("r2_score:",r2_score(y_test, ridge_predict))

# Calculate and print the Mean Absolute Error (MAE)
print("MAE:", mean_absolute_error(y_test, ridge_predict))

# Calculate and print the Mean Squared Error (MSE)
print("MSE:", mean_squared_error(y_test, ridge_predict))

print()

# Print the coefficients of the linear regression model
print("Coef:",ridge.coef_)

# Print the intercept of the linear regression model
print("Intercept:",ridge.intercept_)

# Create a Ridge regression model with a specified alpha value and solver
ridge_tuned = Ridge(alpha=0.3, solver='cholesky')

# Fit the Ridge model to the training data
ridge_tuned.fit(X_train, y_train)

# Make predictions on the test data using the tuned Ridge model
ridge_predict_tuned = ridge.predict(X_test)

# Calculate and print the R-squared (r2) score to evaluate model performance
print("r2_score:",r2_score(y_test, ridge_predict_tuned))

# Calculate and print the Mean Absolute Error (MAE) to measure prediction accuracy
print("MAE:", mean_absolute_error(y_test, ridge_predict_tuned))

# Calculate and print the Mean Squared Error (MSE) to assess prediction accuracy
print("MSE:", mean_squared_error(y_test, ridge_predict_tuned))

print()

# Print the coefficients of the linear regression model
print("Coef:",ridge_tuned.coef_)

# Print the intercept of the linear regression model
print("Intercept:",ridge_tuned.intercept_)

# Create Lasso regression with default parameters

lasso = Lasso()

# Fit model with train data
lasso.fit(X_train, y_train)

# Make prediction on test data
lasso_pred = lasso.predict(X_test)

# Calculate and print the R-squared (r2) score to evaluate model performance
print("r2_score:",r2_score(y_test, lasso_pred))

# Calculate and print the Mean Absolute Error (MAE) to measure prediction accuracy
print("MAE:", mean_absolute_error(y_test, lasso_pred))

# Calculate and print the Mean Squared Error (MSE) to assess prediction accuracy
print("MSE:", mean_squared_error(y_test, lasso_pred))

print()

# Print the coefficients of the linear regression model
print("Coef:",lasso.coef_)

# Print the intercept of the linear regression model
print("Intercept:",lasso.intercept_)

# Create Lasso regression with alpha value
lasso_tuned = Lasso(alpha=0.3)

# Fit the model on train data
lasso_tuned.fit(X_train, y_train)

# Prediction on test data
lasso_tuned_pred = lasso_tuned.predict(X_test)

# Calculate and print the R-squared (r2) score to evaluate model performance
print("r2_score:",r2_score(y_test, lasso_tuned_pred))

# Calculate and print the mean absolute error(MSE) score to evaluate model performance
print("MAE:", mean_absolute_error(y_test, lasso_tuned_pred))

# Calculate and print the Mean Squared Error (MSE) to assess prediction accuracy
print("MSE:", mean_squared_error(y_test, lasso_tuned_pred))

# Import DecisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor

# Create a DecisionTreeRegressor model
dtr = DecisionTreeRegressor()

# Train the model using the training data
dtr.fit(X_train, y_train)

# Train the model using the training data
dtr_pred = dtr.predict(X_test)

# Calculate and print the R-squared (r2) score to evaluate model performance
print("r2_score:",r2_score(y_test, dtr_pred))

# Calculate and print the mean absolute error(MSE) score to evaluate model performance
print("MAE:", mean_absolute_error(y_test, dtr_pred))

# Calculate and print the Mean Squared Error (MSE) to evaluate prediction errors
print("MSE:", mean_squared_error(y_test, dtr_pred))

# Create Decision tree with max depth = 4
dtr_tuned = DecisionTreeRegressor(max_depth=4)

# Fit model with train data
dtr_tuned.fit(X_train, y_train)

# Make prediction on test data
dtr_tuned_pred = dtr_tuned.predict(X_test)

# Calculate and print the R-squared (r2) score to evaluate model performance
print("r2_score:",r2_score(y_test, dtr_tuned_pred))

# Calculate and print the mean absolute error(MSE) score to evaluate model performance
print("MAE:", mean_absolute_error(y_test, dtr_tuned_pred))

# Calculate and print the Mean Squared Error (MSE) to evaluate prediction errors
print("MSE:", mean_squared_error(y_test, dtr_tuned_pred))

# Import Random Forest from sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Create Random forest regression on default parameters
rnd = RandomForestRegressor()

# Fit model on train data
rnd.fit(X_train, y_train)

# Make prediction on test data
rnd_pred = rnd.predict(X_test)

# Calculate and print the R-squared (r2) score to evaluate model performance
print("r2_score:",r2_score(y_test, rnd_pred))

# Calculate and print the mean absolute error(MSE) score to evaluate model performance
print("MAE:", mean_absolute_error(y_test, rnd_pred))

# Calculate and print the Mean Squared Error (MSE) to evaluate prediction errors
print("MSE:", mean_squared_error(y_test, rnd_pred))

# Create Random Forest regression with tuned parameters
rnd_tuned = RandomForestRegressor(n_jobs=-1, max_features=5, min_samples_split=3)

# Fit model on train data
rnd_tuned.fit(X_train, y_train)

# Make prediction on test data
rnd_tuned_pred = rnd_tuned.predict(X_test)

# Calculate and print the R-squared (r2) score to evaluate model performance
print("r2_score:",r2_score(y_test, rnd_tuned_pred))

# Calculate and print the mean absolute error(MSE) score to evaluate model performance
print("MAE:", mean_absolute_error(y_test, rnd_tuned_pred))

# Calculate and print the Mean Squared Error (MSE) to evaluate prediction errors
print("MSE:", mean_squared_error(y_test, rnd_tuned_pred))

# Parameters
params_grid = {"max_features": [4,5,6,7,8,9,10],
              "min_samples_split": [2,3,10]}

# Find best parameter for model
grid_search = GridSearchCV(rnd_tuned, params_grid, n_jobs=-1, cv=5)

grid_search.fit(X_train, y_train)
