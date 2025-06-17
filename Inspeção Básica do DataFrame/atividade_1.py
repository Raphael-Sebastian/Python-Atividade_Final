#1. Quantas linhas e colunas tem o nosso DataFrame?

# #Info
import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)
# print(df_filmes)
print("dados carregados com sucesso!!!")
print("\n Informações sobre o dataFrame")
print(df_produtos.info())

