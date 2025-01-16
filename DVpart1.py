import numpy as numpy
import matplotlib.pyplot as pyplot
import seaborn as seaborn
import pandas as panda

#data cleaning
data = {
    "name" : ["atiya",np.nan,"me","he",9000],
    "age" : [np.nan,-12,0,1,9]
}

MyDF = pd.DataFrame(data)
MyDF["name"] = MyDF["name"].fillna("unknown")

for i in(MyDF["name"]):
    print(MyDF["name"])


MyDF("name") = MyDF["name"].apply(lambda x : x if isinstance(name,str)else "unknown")
