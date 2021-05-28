# Exercicio 03
print('Exercicio 03')
import random
l1, l2, l3 = [], [], []
l1, l2 = random.sample(range(100), 10), random.sample(range(100), 10)
for x in range(10):
    l3.append(l1[x])
    l3.append(l2[x])
print(f'Lista 01: {l1}')
print(f'Lista 02: {l2}')
print(f'Lista 03: {l3}')