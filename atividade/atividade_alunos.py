import pandas as pd

URL = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
df = pd.read_csv(URL)
df['Pontos_extras'] = df['Notas'].apply(lambda x: x * 0.4)
df['Notas_finais'] = df['Notas'] + df['Pontos_extras']
df['Aprovado_final'] = df['Notas_finais'] > 6
print(df.head())