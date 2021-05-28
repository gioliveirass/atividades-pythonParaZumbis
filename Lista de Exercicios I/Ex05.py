# Exercicio 05
print('Exercicio 05: Calculando Desconto')
preco = int(input('Insira o preço da mercadoria: '))
desconto = int(input('Insira o percentual de desconto: '))
precoPagar = preco - preco * desconto / 100
print(f'O valor a se pagar pela mercadoria é: {precoPagar:.2f} reais')