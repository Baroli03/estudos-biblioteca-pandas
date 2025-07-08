from dados.dados import df_apartamentos


# 1) Calcular a média de quartos por apartamento;
df_media = df_apartamentos['Quartos'].mean()
print(f"O Total de Quartos é {df_media:.2f}")
