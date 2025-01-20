import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as seaborn
import pandas as pd

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
CovidDF = pd.read_csv(url)

print(CovidDF.info())

Country = "India"
Covid_India = CovidDF[CovidDF["location"]==Country]

Covid_India = Covid_India[["date","new_cases","new_deaths",]]
Covid_India["date"] = pd.to_datetime(Covid_India["date"])

plt.figure(figsize=(8,6))
plt.plot(Covid_India["date"],Covid_India["new_cases"],label="New Cases",color="blue")
plt.plot(Covid_India["date"],Covid_India["new_deaths"],label="New Deaths",color="red")
plt.title("Covid case analysis")
plt.xlabel("Date")
plt.ylabel("Count")
plt.grid(True)
plt.legend()
plt.show()