# Exercicio 09
print('Exercicio 09: Calculando aluguel do carro.')
km = int(input('Insira a quantidade de km percorridos: '))
dia = int(input('Insira a quantidade de dias pelos quais o carro foi alugado: '))
preco = (dia * 60) + (0.15 * km)
print(f'O total a pagar é: {preco:.2f} reais')