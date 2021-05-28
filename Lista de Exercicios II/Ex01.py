# Exercicio 01
print('Exercicio 01: Verificando um triângulo.')
a = int(input('Informe o valor do lado 1: '))
b = int(input('Informe o valor do lado 2: '))
c = int(input('Informe o valor do lado 3: '))
if (b-c) < a < b + c and (a-c) < b < a + c and (a-b) < c < a + b:
    if a == b == c:
        print('É um triangulo equilátero!')
    elif a == b  or a == c or b == c:
        print('É um triangulo isósceles!')
    else:
        print('É um triangulo escaleno!')
else:
    print('Não é um triângulo.')