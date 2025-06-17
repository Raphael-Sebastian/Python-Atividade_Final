# 10. Quais são os produtos da categoria 'Verdura'?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

produtos_selecionados = df_produtos[df_produtos["Categoria"] == "Verdura"]
print(f"\nProdutos da categoria Verdura")
print(produtos_selecionados)