#17. Liste os produtos ordenados pela Data_Ultima_Reposicao (do mais recente para o mais antigo) e,
# para datas iguais, pelo nome do produto em ordem alfabética.

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

df_ordenado = df_produtos.sort_values(
    by=["Data_Ultima_Reposicao", "Produto"],
    ascending=[False,True]
)
print(df_ordenado)