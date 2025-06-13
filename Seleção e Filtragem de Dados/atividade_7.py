import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

produtos_selecionados = df_produtos[["Produto"]]
print(f"\nDataFrame com a coluna Produto")
print(produtos_selecionados)