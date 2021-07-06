# Data Manipul ations
import pandas as pd
df=pd.read_csv("AB_NYC_2019.csv")
print(df.head(3))

df2=df.set_index('id')
print(df2.head(3))

# group
df3=df.groupby('room_type').mean()
print(df3.reset_index())

# sorting
print(df3.sort_index(ascending=False))

print(df.sort_values('host_name'))

# unique
print(df.neighbourhood_group.unique())

# group counts
print(df.neighbourhood_group.value_counts())

# rank
dfp=df.sort_values('price', ascending=False)
print(dfp[['id', 'host_name', 'price']].head(5))

dfp['price_rank']=dfp.price.rank(method='average', ascending=False)
print(dfp)