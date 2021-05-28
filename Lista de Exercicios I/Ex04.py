# Exercicio 04
print('Exercicio 04: Calculando aumento de salário.')
salario = int(input('Insira o valor do salário: '))
aumento = int(input('Insira a porcentagem do aumento do salário: '))
salarioNovo = salario + salario * aumento / 100
print(f'O novo salário é de {salarioNovo:.2f} reais')