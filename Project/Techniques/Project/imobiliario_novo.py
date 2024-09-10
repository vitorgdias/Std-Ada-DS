import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as plt

df = pd.read_csv("C:\\Users\\diogo\\OneDrive\\Documentos\\Profissional\\projeto_dados_imobiliarios\\mercadoimobiliario.csv", sep = ';')


#checando o status do DataFrame
df.info()

#obtendo os valores unicos de cada coluna para observar qual é a coluna mais fácil para se trabalhar
print(df['Data'].nunique())
print(df['Info'].nunique())

#Como o Dataset é brasileiro, precisa-se transformar as virgulas em pontos para se trabalhar da melhor forma
df['Valor'] = df['Valor'].str.replace(',', ".")


