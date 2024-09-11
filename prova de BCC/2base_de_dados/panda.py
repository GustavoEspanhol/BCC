import pandas as pd

df = pd.read_csv("pokemon.csv")

print(df.head(7).sort_values(by=["Name","#"], ascending=[False,True]))

df_ordenadanumero = df.sort_values(by="#", ascending=False)
print(df_ordenadanumero)

df_lendarios = df.query("Legendary == True")
print(df_lendarios)

df_maiorHP = df["HP"].max()
print(df_maiorHP)

df_somaAttack = df["Attack"].count()
print(df_somaAttack)

df_agrupamentoDefense = df.groupby("Defense")["Name"].count()
print(df_agrupamentoDefense)

df_filtrada = df.query("Legendary == True and HP > 100")
df_final = df[["Name","HP"]]
print(df_final)