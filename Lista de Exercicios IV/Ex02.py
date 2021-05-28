# Exercicio 02
print('Exercicio 02')
import random
num, impares, pares = [], [], []
num = random.sample(range(100), 20)
for x in num:
    if x%2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f'Números: {num}')
print(f'Impares: {impares}')
print(f'Pares: {pares}')