import csv

file_path = 'Project\Techniques\Project\mercadoimobiliario.csv'

with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)

print(f'Número de linhas: {row_count}')