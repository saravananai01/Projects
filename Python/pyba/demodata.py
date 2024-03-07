import pandas as pd
import matplotlib.pyplot as mpl

# data={
#     "Name":["Arun","Hariharn","Prasanth"],
#     "Location":["Keeranur","Keeranur","Perambalur"]
# }

# pt=pd.DataFrame(data)

# print(pt)

data=pd.read_csv("laptop_price.csv",encoding='latin-1')

dispaly1=pd.DataFrame(data)

dispaly1.plot(kind='bar',
        x='Company',
        y='Price_euros',
        color='red')

mpl.title("Laptop Price Graph")
mpl.show()

# To First Viwe Data :
# print(df.head())

# To Last View Data :
# print(df.tail())

# To First & Last View Data :

# print(df.head(10))
# print(df.tail(10))
