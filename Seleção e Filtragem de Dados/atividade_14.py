#14. Selecione os produtos que são 'Fruta' OU têm Estoque_Kg maior que 150 Kg

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

print("\nCategoria Frutas")
print(df_produtos[df_produtos["Categoria"] == "Fruta"])
print("\nProdutos que são maiores que 150Kg ")
print(df_produtos[df_produtos["Estoque_Kg"] > 150])
