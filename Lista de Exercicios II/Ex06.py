# Exercicio 06
print('Exercicio 06: Calculando salário.')
ganhoPorHora = int(input('Digite quanto você ganha por hora: '))
horasTrabMes = int(input('Digite quantas horas você trabalha por mês: '))
salarioBruto = ganhoPorHora * horasTrabMes
ir = salarioBruto * 11 / 100
inss = salarioBruto * 8 / 100
sindicato = salarioBruto * 5 / 100
salarioLiquido = salarioBruto - ir - inss - sindicato
print(f'+ Salário Bruto: R$ {salarioBruto:.2f}')
print(f'- IR (11%): R$ {ir:.2f}')
print(f'- INSS (8%): R$ {inss:.2f}')
print(f'- Sindicato (5%): R$ {sindicato:.2f}')
print(f'= Salário Liquido: R$ {salarioLiquido:.2f}')