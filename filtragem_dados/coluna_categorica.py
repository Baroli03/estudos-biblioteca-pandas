from dados.dados import dados_copy

dados = dados_copy.copy()

dados['Descricao'] = dados['Tipo'] +' em ' + dados['Bairro'] + ' com ' + \
                     dados['Quartos'].astype(str) + ' Quarto(s)' + ' e ' + dados['Vagas'].astype(str) + ' Vaga(s) de garagem.'
print(dados.head())
# suites_false = dados.query('Suites == 0').index
# suites_true = dados.query('Suites > 0').index
# dados.loc[suites_true, 'Possui_suite'] = True
# dados.loc[suites_false, 'Possui_suite'] = False
dados['Possui_suite'] = dados['Suites'].apply(lambda x: True if x > 0 else False)
dados.to_csv('dados.csv')