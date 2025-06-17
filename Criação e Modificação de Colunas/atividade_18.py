#18. Crie uma nova coluna chamada Valor_Total_Estoque que seja o resultado da multiplicação de
# Preco_Kg por Estoque_Kg

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

df_produtos["Valor_Total_Estoque"] = df_produtos["Preco_Kg"] * df_produtos["Estoque_Kg"]

print(df_produtos[["Produto","Preco_Kg","Estoque_Kg","Valor_Total_Estoque"]].head())