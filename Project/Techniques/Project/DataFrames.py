import csv
import pandas as pd
import numpy as np

file_path = 'Project\Techniques\Project\mercadoimobiliario.csv'

with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)

print(f'Número de linhas: {row_count}')

df = pd.read_csv('Project\Techniques\Project\mercadoimobiliario.csv', delimiter=',', header=0)
print(df.columns)

df.head()
# Criar a coluna Estado
df['Estado'] = df['Info'].str[-2:]

# Filtrar os dados que terminam com 'ma'
df_ma = df[df['Info'].str.endswith('ma')]

df.head()
print(df_ma.head())