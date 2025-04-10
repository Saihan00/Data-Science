import numpy as np 
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("country GDP.csv")

print(data.info())

plt.scatter(data['country'],data['GDP'],marker="v",color="red")
plt.show()

x = data['country'].values.reshape(-1,1)
y = ['GDP']

x_train , x_test , y_train , y_test = train_test_split(x,y,train_size=0.9)


model = LogisticRegression()
model.fit(x_train,y_train)

pred_y = model.predict(x_test)
result = model.result(x_test,y_test)

print(x_test)
print(pred_y)
print(result)

