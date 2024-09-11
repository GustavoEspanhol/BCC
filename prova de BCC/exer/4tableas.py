import pandas as pd

df = pd.read_csv("https://drive.google.com/u/3/uc?id=1id-MxIdlA5pG0iJROsmxLzsBahvtNExc&export=download", sep = ';' ) 

#df = df.sort_values(by="Codigo", ascending=False)

#df = df.sort_values(by=["Codigo","Salario"], ascending=[False,True])


#df = df["Salario"].mean()
#df = df["Salario"].max()

#df = df.groupby("Idade_Anos")["Salario"].mean()

#df = df.groupby("Idade_Anos")["Salario"].count()

df = df[["Idade_Anos","Salario"]]






print(df)
