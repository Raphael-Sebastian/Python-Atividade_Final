#29. Calcule a soma das Vendas_Ultima_Semana_Kg e o Valor_Total_Estoque médio para cada Categoria.


import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

resultado = df_produtos.groupby('Categoria').agg({
    'Vendas_Ultima_Semana_Kg': 'sum',
    'Valor_Total_Estoque': 'mean'
})

print(resultado)