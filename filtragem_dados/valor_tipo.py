from dados.dados import dados


# Qual o valor médio de Alugiel por Tipo de Imóvel?

dados_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
print(dados_preco_tipo)

