# Exercicio 03
print('Exercicio 03: Calculando total em segundos.')
dias = int(input('Insira a quantidade de dias: '))
horas = int(input('Insira a quantidade de horas: '))
minutos = int(input('Insira a quantidade de minutos: '))
segundos = int(input('Insira a quantidade de segundos: '))
total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(f'Total: {total} segundos.')