# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras

# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
def verbing(s):
  if len(s) >= 3:
    if s[-3:] == 'ing':
      string = s + 'ly'
    else: string = s + 'ing'
  else:
    string = s
  return string

# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
  inicioNot = s.find('not')
  inicioBad = s.find('bad')
  return s[:inicioNot] + 'good' + s[inicioBad+3:] \
         if inicioBad > inicioNot \
         else s

# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
# a_inicio + b_inicio + a_final + b_final
def inicio_final(a, b):
  # calculando pedaços de A
  if len(a) % 2 == 0:
    primeiroPedacoA = a[:len(a)//2]
    segundoPedacoA = a[len(a)//2:]
  else:
    primeiroPedacoA = a[:(len(a)//2)+1]
    segundoPedacoA = a[(len(a)//2)+1:]
  # calculando pedaços de B
  if len(b) % 2 == 0:
    primeiroPedacoB = b[:len(b)//2]
    segundoPedacoB = b[len(b)//2:]
  else:
    primeiroPedacoB = b[:(len(b)//2)+1]
    segundoPedacoB = b[(len(b)//2)+1:]
  
  return primeiroPedacoA + primeiroPedacoB + segundoPedacoA + segundoPedacoB

# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
def zf(n):
  numInvertido, numIndice, numContador = str(n)[::-1], 0, 0
  while True:
    if numInvertido[numIndice] == '0':
      numContador += 1
    else:
      break
    numIndice += 1
  return numContador

# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
  doisQtd = 0
  for numero in range(0, n):
    for indiceNumero in range(len(str(numero))):
      if str(numero)[indiceNumero:indiceNumero+1] == '2':
        doisQtd += 1
  return doisQtd

# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
  potencia = 0
  while True:
    if str(2**potencia)[:len(str(n))] == str(n):
      resposta = potencia
      break
    potencia += 1
  return resposta

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print ()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print ()
  print ('inicio_final')
  test(inicio_final('abcd', 'xy'), 'abxcdy')
  test(inicio_final('abcde', 'xyz'), 'abcxydez')
  test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

  print ()
  print ('zeros finais')
  test(zf(10100100010000), 4)
  test(zf(90000000000000000010), 1)

  print ()
  print ('conta 2')
  test(conta2(20), 2)
  test(conta2(999), 300)
  test(conta2(555), 216)

  print ()
  print ('inicio p2')
  test(inip2(7), 46)
  test(inip2(133), 316)
  test(inip2(1024), 10)
  
if __name__ == '__main__':
  main()
