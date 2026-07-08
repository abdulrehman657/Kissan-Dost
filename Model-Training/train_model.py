import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import joblib

df = pd.read_csv('pak_crop_data.csv')

X = df.drop(columns=['Yield_Maunds'])
y = df['Yield_Maunds']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)


joblib.dump(model, 'crop_model.pkl')
print("Model Saved Successfully")