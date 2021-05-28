# Exercicio 03
ano = 0
a = 80000
b = 200000
while a < b:
    a = a + a * 3 / 100
    b = b + b * 1.5 / 100
    ano = ano + 1
print(f'A cidade A demorará {ano} anos para ultrapassar a cidade B.')