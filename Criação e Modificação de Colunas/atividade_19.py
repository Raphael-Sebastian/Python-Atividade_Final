#19. Suponha que todos os produtos da categoria 'Fruta' terão um aumento de 5% no preço. Atualize a
# coluna Preco_Kg para refletir esse aumento APENAS para as frutas. (Cuidado para não alterar os
# preços dos legumes e verduras).

import pandas as pd

url_produtos = "produtos_mercado.csv"

df_produtos = pd.read_csv(url_produtos)

df_produtos.loc[df_produtos["Categoria"] == "Fruta", "Preco_Kg"] *= 1.05

print(df_produtos)