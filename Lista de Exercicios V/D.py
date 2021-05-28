# Questão D (Resposta: 7995)
resposta = 0
for num in range(18644, 33088):
    if '2' in str(num) and '7' not in str(num):
        resposta = resposta + 1
print(f'Quantidade de números sortudos: {resposta}')