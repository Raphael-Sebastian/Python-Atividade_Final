# 5. Exiba as 3 últimas linhas do DataFrame
import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)
print("\n Últimas 3 linhas do DataqFrame de filmes:")
print(df_produtos.tail(3))