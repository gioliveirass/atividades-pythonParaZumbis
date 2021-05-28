# Questão B (Resposta: 48)
contador = 0
for i in range(1,10):
    if i != 3:
        for j in range(1,7):
            contador = contador + 1
print(f"Quantidade de oi's: {contador}")