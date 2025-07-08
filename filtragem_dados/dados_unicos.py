from dados.dados import df_apartamentos

# 2) Conferir quantos bairros únicos existem na nossa base de dados;
df_bairros = df_apartamentos['Bairro'].nunique()
print(df_bairros)
