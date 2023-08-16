import pandas as pd
data=pd.read_csv("C:/Users/SPTINT-16/Desktop/dataset/IRIS1.csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data["sepal_width"])
print(data.info())
print(data.dtypes)
print(data.count())
