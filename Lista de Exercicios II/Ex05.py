# Exercicio 05
print('Exercicio 05: Exibindo o maior e o menor número.')
n1 = int(input('Número 01: '))
n2 = int(input('Número 02: '))
n3 = int(input('Número 03: '))
if n1>=n2 and n1>=n3: #Calculando maior num
    print(f'O maior número é {n1}')
elif n2>n1 and n2>=n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior número é {n3}')
if n1<=n2 and n1<=n3: #Calculando menor num
    print(f'O menor número é {n1}')
elif n2<n1 and n2<=n3:
    print(f'O menor número é {n2}')
else:
    print(f'O menor número é {n3}')