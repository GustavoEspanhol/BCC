import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")

df_mediaHP = df["HP"].mean()
print(df_mediaHP)

df_percentilHP = np.percentile(df["HP"], q=50)
print(df_percentilHP)

#adicionando colunas
df["Dano"] = df["Attack"]*df["Sp. Atk"]
print(df["Dano"].head(5))

df.boxplot(column="HP")

coeficiente_de_correlação = df["Attack"].corr(df["Sp. Atk"])
print(coeficiente_de_correlação)#sempre entre -1 e 1

x = df["Attack"]
y = df["Sp. Atk"]
plt.plot(x,y,'.')

                #primeiro grau
(a,b) = np.polyfit(x, y, deg=1)
print(a,b)

z = a*15+b
print(z)

coef_cor = df["HP"].corr(df["Defense"])
coeficiente_de_determinação = coef_cor**2
print(coeficiente_de_determinação)



