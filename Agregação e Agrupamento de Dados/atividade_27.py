#27. Para cada Categoria, qual foi o produto com maior Vendas_Ultima_Semana_Kg?

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)


indices = df_produtos.groupby('Categoria')['Vendas_Ultima_Semana_Kg'].idxmax() #idxmax == encontra o índice do produto com maior venda na última semana em cada categoria


resultado = df_produtos.loc[indices, ['Categoria', 'Produto', 'Vendas_Ultima_Semana_Kg']]

print(resultado)
