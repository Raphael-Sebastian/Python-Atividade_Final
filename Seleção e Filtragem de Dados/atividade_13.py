# 13. Quais produtos são fornecidos pela 'Fazenda Sol Nascente' E são da categoria 'Fruta'?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

fornecedor_filtrado = df_produtos.loc[df_produtos["Fornecedor"] == "Fazenda Sol Nascente"]

produtos_filtrados = fornecedor_filtrado.loc[fornecedor_filtrado["Categoria"] == "Fruta"]

print(produtos_filtrados)