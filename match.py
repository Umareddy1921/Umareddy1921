import pandas as pd
data=pd.read_csv("C://Users/RK/Desktop/manu/matches.csv")
print(data)
print(data.head())
print(data.tail())
print(data.head(15))
print(data.tail(20))
print(data[500:])
print(data[:100])
print(data[14:63])
print(data[data['Season']==2008].shape[0])
print(data[data['Season']==2008])
print(data[data['Winner']=='Chennai Super Kings'])
print(data[data['City']=='Delhi'])
 