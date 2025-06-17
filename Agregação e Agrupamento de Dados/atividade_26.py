#26. Qual é o estoque total (soma de Estoque_Kg) para cada Fornecedor?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

estoque_total = df_produtos.groupby("Fornecedor")["Estoque_Kg"].sum()
print(estoque_total)