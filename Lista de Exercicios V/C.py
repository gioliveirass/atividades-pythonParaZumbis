# Questão C (Resposta: 183)
cont = 0
for num in range(1067, 3628):
    if num%2 == 0 and num%7 == 0:
        cont = cont + 1
print(f'Quantidade de números pares e divisíveis por 7: {cont}')