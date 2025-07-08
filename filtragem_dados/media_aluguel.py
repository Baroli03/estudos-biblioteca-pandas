from dados.dados import df_apartamentos
from matplotlib import pyplot as plt

# 3) Analisar quais bairros possuem a média de valor de aluguel mais elevadas
df_valor_aluguel = df_apartamentos[["Bairro", "Valor"]]
df_valor_aluguel = df_valor_aluguel.groupby("Bairro")['Valor'].mean().sort_values(ascending=False)
print(df_valor_aluguel)

#4) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.
df_top_5 = df_valor_aluguel.head().sort_values(ascending=True)
df_top_5.plot(kind='barh', figsize=(18,9), fontsize=12, xlabel='Valor', ylabel='Bairros')
plt.show()