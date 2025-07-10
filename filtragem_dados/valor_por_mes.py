import pandas as pd
from dados.dados import dados_copy

dados_copy['Valor_por_mês'] = dados_copy['Valor'] + dados_copy['Condominio']
dados_copy['Valor_por_ano'] = (dados_copy['Valor_por_mês'] * 12) + dados_copy['IPTU']
print(dados_copy.head())