#23. O 'Kiwi' está com Estoque_Kg ausente. Preencha esse valor com 0 (zero)

import pandas as pd

url_produtos = "Python-Atividade_Final/produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

é_kiwi = df_produtos["Produto"] == "Kiwi"
df_produtos.loc[é_kiwi, "Estoque_Kg"] = 0