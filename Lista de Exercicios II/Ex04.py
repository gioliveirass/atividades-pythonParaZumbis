# Exercicio 04
print('Exercicio 04: Exibindo o maior número.')
n1 = int(input('Número 01: '))
n2 = int(input('Número 02: '))
n3 = int(input('Número 03: '))
if n1>=n2 and n1>=n3:
    print(f'O maior número é {n1}')
elif n2>n1 and n2>=n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior número é {n3}')