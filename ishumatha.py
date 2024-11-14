import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users/RK/Downloads/uma.csv")
product_per_city=data.groupby('City').size().reset_index(name='Product_Count')
print(product_per_city)
plt.bar(product_per_city['City'], product_per_city['Product_Count'])
plt.xlabel('City')
plt.ylabel('Number of Products')
plt.title('Number of Products in each City')
plt.show()
