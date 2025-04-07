import numpy as np 
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("insurance_data.csv")
print(data.info())

plt.scatter(data['age'],data['bought_insurance'],marker="v",color="red")
plt.show()
