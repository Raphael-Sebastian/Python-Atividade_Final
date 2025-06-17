# 9. Exiba os dados do produto com ID_Produto igual a 110 (Limão Tahiti).
import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

produto = df_produtos[df_produtos['ID_Produto'] == 110]
print(produto)