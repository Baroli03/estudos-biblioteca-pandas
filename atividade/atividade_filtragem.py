import pandas as pd

URL = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv"

df = pd.read_csv(URL)

# Conferindo quantos dados Nulos existem
# print(df.isna().sum())
# Fillna Substitui os dados nulos, porem sempre conferir quais dados são para ver se faz sentido
df.fillna(0, inplace=True)
df = df.set_index('Nome')
df.drop("Alice", inplace=True)
df.drop("Carlos", inplace=True)
df_aprovados = df.query("Aprovado == True")
print(df_aprovados.replace(7, 8))

