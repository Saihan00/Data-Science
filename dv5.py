import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as seaborn
import pandas as panda

data ={
    "X":[1,2,3,4,5],
    "Y":[4,7,9,0,5]
}

plt.figure(figsize=(8,6))
plt.title("my data using scatter plot")
plt.xlabel("X-Label")
plt.ylabel("Y-Label")
plt.scatter(data["X"],data["Y"])
plt.show()