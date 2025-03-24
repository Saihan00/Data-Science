import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv ("petrol_consumption.csv")


x = dataset[['Petrol_ tax','Average_income','Paved_highways','Population_Driver_licence(%)']]

y = dataset['Petrol_Consumption']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.21,random_state=0)

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_predict=regressor.predict(x_test)
df=pd.Dataframe({"Actual: ": y_test,"Predicted: ": y_predict})
print(df)