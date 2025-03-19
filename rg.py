import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



ages = np.array([1,2,3,4,5,6,7,8])
heights = np.array([3.5,3.6,4.1,4.9,3.3,3.0,5.8,6.1])

model = LinearRegression()
model.fit(ages,heights)

predicated_height = model.predict(ages)

plt.scatter(ages,heights,color="blue",label="Actual height")
plt.plot(ages,predicted_height,color="red",label="Regression Line")

plt.xlabel("age")
plt.ylabel("heights")
plt.label("Age_height Prediction using Regression")
plt.legend()
plt.show()