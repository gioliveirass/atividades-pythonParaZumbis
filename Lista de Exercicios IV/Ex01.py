# Exercicio 01
print('Exercicio 01')
import random
num = []
min, max = 100, 0
num = random.sample(range(100), 10)
for x in num:
    if x >= max:
        max = x
    if x <= min:
        min = x
print(f'Todos os números: {num}')
print(f'Menor valor: {min}')
print(f'Maior valor: {max}')