# 3. Quais são os tipos de dados de cada coluna? A coluna Data_Ultima_Reposicao está no formato

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

print("\n Informações sobre o dataFrame")
print(df_produtos.info())

print(f"\n O dataframe de produtos tem esses dados {df_produtos.shape[1]}")

