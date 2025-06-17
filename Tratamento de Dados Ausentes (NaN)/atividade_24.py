#24. Após os preenchimentos, verifique novamente se ainda existem valores ausentes.

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

kiwi = df_produtos["Produto"] == "Kiwi"
df_produtos.loc[kiwi, "Estoque_Kg"] = 0