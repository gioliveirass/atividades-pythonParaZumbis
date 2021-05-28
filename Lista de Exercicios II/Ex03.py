# Exercicio 03
print('Exercicio 03: Calculando a multa do João Papo-de-Pescador.')
peso = int(input('Peso do peixe em quilos: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O peixe excedeu {excesso:.2f} quilos e João deverá pagar uma multa de {multa:.2f} reais.')
else:
    excesso, multa = 0, 0
    print('O peixe não excedeu o limite de peso e João não será multado.')