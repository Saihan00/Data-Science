import numpy as np
import matplotlib.pyplot as plt
import seaborn as seaborn
import pandas as pd


Titanic = pd.read_csv("Titanic Dataset.csv")
print (Titanic.info())

meanage = np.mean(Titanic["Age"])
print(round(meanage))