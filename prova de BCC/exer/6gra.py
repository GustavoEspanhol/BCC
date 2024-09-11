import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download")

plt.plot(df["Trabalho"],df["Prova 2"], '.')

[a, b] = np.polyfit(df["Trabalho"], df["Prova 2"], deg=1)
x = df["Trabalho"]
y = a*x+b
plt.plot(x,y,'r')
plt.show()
