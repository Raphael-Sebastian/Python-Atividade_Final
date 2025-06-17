# 2. Quais são os nomes de todas as colunas?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)
 
 
print("\n Informações sobre o dataFrame")
print(df_produtos.info())

print(f"\n O dataframe de produtos tem {df_produtos.shape[1]}")