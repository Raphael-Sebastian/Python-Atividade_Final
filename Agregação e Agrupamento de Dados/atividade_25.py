#25. Qual é o preço médio por Categoria de produto?


import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)


preco_medio = df_produtos.groupby("Categoria")["Preco_Kg"].mean() #Agrupa o DataFrame df em grupos baseados nos valores únicos da coluna "Categoria". Ou seja, ele separa as linhas em grupos onde a categoria é igual.
print(preco_medio)
