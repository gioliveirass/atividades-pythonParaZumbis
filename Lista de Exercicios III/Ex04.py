# Exercicio 04
elemento = int(input('Insira um número inteiro: '))
cont = 2
primeiro, segundo = 1, 1
while cont < elemento:
    primeiro, segundo = segundo, primeiro + segundo
    cont = cont + 1
print(f'Número de Fibonacci: {segundo}')