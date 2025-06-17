
#22. O 'Morango' está com Preco_Kg ausente. Preencha esse valor ausente com a média de preço de todos os outros produtos da categoria 'Fruta

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)


frutas = df_produtos[df_produtos["Categoria"] == "Fruta"]

media_frutas = frutas["Preco_Kg"].mean()

morango_faltantando = df_produtos["Produto"] == "Morango"
df_produtos.loc[morango_faltantando, "Preco_Kg"] = df_produtos.loc[morango_faltantando, "Preco_Kg"].fillna(media_frutas)
