from dados.dados import df_apartamentos

# Objetivo: Filtrar Apartamentos que possuem 2 Quarto ou mais e Aluguel menor que 3000 e mais que 70 m²

# Minha resposta para a atividade:
df_2q_ate_3000_70m = df_apartamentos.query('Quartos >= 2 and Valor < 3000 and Area > 70')
# Outra aprendida no curso:
selecao = (df_apartamentos['Quartos'] >= 2) & (df_apartamentos['Valor'] < 3000) & (df_apartamentos['Area'] > 70)
df_2q_ate_3000_70m_forma2 = df_apartamentos[selecao]
print(df_2q_ate_3000_70m_forma2)

