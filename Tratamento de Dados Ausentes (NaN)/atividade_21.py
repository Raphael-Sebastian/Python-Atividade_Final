# 21. Verifique quantas valores ausentes (NaN) existem em cada coluna do DataFrame.

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

# Supondo que você já tenha um DataFrame chamado df
valores_ausentes = df_produtos.isna().sum()
print(valores_ausentes)
