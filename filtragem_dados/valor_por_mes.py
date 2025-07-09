import pandas as pd
from dados.dados import dados

# Criar a cópia
dados_copy = dados.copy()

# Preencher valores nulos da forma recomendada
dados_copy['Valor'] = dados_copy['Valor'].fillna(0)
dados_copy['Condominio'] = dados_copy['Condominio'].fillna(0)
dados_copy['IPTU'] = dados_copy['IPTU'].fillna(0)

dados_copy['Valor_por_mês'] = dados_copy['Valor'] + dados_copy['Condominio']
dados_copy['Valor_por_ano'] = (dados_copy['Valor_por_mês'] * 12) + dados_copy['IPTU']
print(dados_copy.head())