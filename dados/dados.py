import pandas as pd

# Qual o valor médio de Alugiel por Tipo de Imóvel?


# .mean(numeric_only=True) para que seja calculado a média somente dos itens númericos
# .sort_values('Valor') para ordenar os itens da coluna valor
# dados_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
# dados_preco_tipo.plot(kind='barh', figsize=(20,10), color='purple')


# Removendo os imóveis Comerciais
# print(dados.Tipo.unique())

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

df = pd.read_csv(url, sep=';')


imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

dados = df.query('@imoveis_comerciais not in Tipo')
# Criar a cópia
dados_copy = dados.copy()

# Preencher valores nulos da forma recomendada
dados_copy['Valor'] = dados_copy['Valor'].fillna(0)
dados_copy['Condominio'] = dados_copy['Condominio'].fillna(0)
dados_copy['IPTU'] = dados_copy['IPTU'].fillna(0)

df_apartamentos = dados.query('Tipo == "Apartamento"')