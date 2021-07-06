import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv('heart.csv')

# Plots
graf=df.plot.scatter("age", "trestbps")
plt.show()

# line plots
ages=df.groupby("age").median().reset_index()
ages.plot.line('age', ['chol', 'trestbps'])
plt.show()

# save in png
# plot.png


