# Exercicio 05
n1 = int(input('Insira um número inteiro positivo: '))
n2 = int(input('Insira outro número inteiro positivo: '))
c = 0
while n1%n2 != 0:
    n1, n2 = n2, n1%n2
    c = c + 1
print(f'O MDC entre os dois números é: {n2}')