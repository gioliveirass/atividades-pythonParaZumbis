# Exercicio 10
print ('Exercicio 10: Tempo de vida de um fumante.')
cigarro = int(input('Cigarros fumados por dia: '))
anos = int(input('Anos fumando: '))
tempoPerdido = ((anos * 365 * cigarro) * 10) / 60 / 24
print(f'O total de dias perdidos é: {tempoPerdido:.2f}')