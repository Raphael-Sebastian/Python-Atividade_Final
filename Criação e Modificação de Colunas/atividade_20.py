# 20. Crie uma coluna chamada Status_Estoque que contenha:
# ○ 'Alto' se Estoque_Kg > 150
# ○ 'Médio' se Estoque_Kg > 50 e <= 150
# ○ 'Baixo' se Estoque_Kg <= 50

import pandas as pd
import numpy as np

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

df_produtos["Status_Estoque"] = "indefinido"

df_produtos.loc[df_produtos["Estoque_Kg"] > 150, "Status_Estoque"] = "Alto"
df_produtos.loc[df_produtos["Estoque_Kg"] > 50, "Status_Estoque"] = "Médio"
df_produtos.loc[df_produtos["Estoque_Kg"] <= 50, "Status_Estoque"] = "Baixo"

print(df_produtos[["Nome_Produto", "Estoque_Kg", "Status_Estoque"]].head())
