import pandas as pd

df = pd.read_csv("dados.csv")

print("Primeiras linhas do CSV:")
print(df.head(), "\n")

print("Resumo estatístico:")
print(df.describe(), "\n")

print("Contagem de valores nulos:")
print(df.isnull().sum())