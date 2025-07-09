from dados.dados import df_apartamentos

# Objetivo: Filtrar Apartamentos que possuem 1 Quarto e Aluguel menor que 1200

# Minha resposta para a atividade:
df_1q_ate_1200 = df_apartamentos.query('Quartos == 1 and Valor < 1200')
# print(df_1q_ate_1200.head())
# Outra aprendida no curso:
selecao1 = df_apartamentos['Quartos'] == 1
df_1q_ate_1200_forma2 = df_apartamentos[selecao1]
selecao2 = df_apartamentos['Valor'] < 1200
selecao_final = (selecao1) & (selecao2)
df_1q_ate_1200_forma2 = df_apartamentos[selecao_final]
print(df_1q_ate_1200_forma2)

df_1q_ate_1200.to_csv('dados_apartamentos_1200.csv', index=False, sep=';')