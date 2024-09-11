import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt

#df = pd.read_csv("https://drive.google.com/u/1/uc?id=1pygGDM-F4quUo2Jl4ri-vJosb3FkRQNx&export=download")


#dfcorr = df['Horas'].corr(df["Nota"])
#print(dfcorr)

#coefciente positivo: diretamente proporcionais
#coeficiente negativo: inversamente proporcionais

#mais perto de 1: maior correlação
#mais perto de 0: menor correlação

#df = pd.read_csv("https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download")
#print(df)

#dfcorr = df["Prova 1"].corr(df["Trabalho"])
#print(dfcorr)

#x = df["Prova 1"]
#y = df["Prova 2"]

#plt.plot(x,y,'.')
#plt.show()

df = pd.read_csv("https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download")

df = np.polyfit(df["Prova 1"], df["Prova 2"], deg=1)
print(df)

a = 1.01010101
b = 19.33252525

y = a*65+b
print(y)