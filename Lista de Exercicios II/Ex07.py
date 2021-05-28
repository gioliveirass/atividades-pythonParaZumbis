# Exercicio 07
print('Exercicio 07: Loja de Tinta.')
area = int(input('Area a ser pintada (em metros quadrados): '))
if(area/3) % 18 != 0:
    latas = int((area/3) / 18) + 1
    preco = latas * 80
else:
    latas = (area/3) / 18
    preco = latas * 80
print(f'Quantidade de latas: {latas}')
print(f'Preço a se pagar: R$ {preco:.2f}')