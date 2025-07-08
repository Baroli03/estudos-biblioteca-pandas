import pandas as pd

df = pd.DataFrame({
   'Animal': ['Cachorro', 'Gato', 'Elefante', 'Cachorro', 'Gato', 'Elefante'],
   'Cor': ['Preto', 'Branco', 'Cinza', 'Marrom', 'Preto', 'Marrom'],
   'Quantidade': [2, 3, 1, 4, 2, 2]
})
print(df.groupby('Cor', sort=True).sum(numeric_only=True))
