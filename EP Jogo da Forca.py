# GIOVANA THAÍS DE OLIVEIRA SILVA (DSM)

# importando bibliotecas necessárias
import requests
from random import choice
import string


# ========================
# INICIALIZANDO VARIÁVEIS
# ========================

# variável com os desenhos da forca
forca = ['''
             +-----+
                   |
                   |
                   |
                   |
                   |
        ============
    ''', '''
             +-----+
             |     |
                   |
                   |
                   |
                   |
        ============
    ''', '''
             +-----+
             |     |
             O     |
                   |
                   |
                   |
        ============
    ''', '''
             +-----+
             |     |
             O     |
             |     |
                   |
                   |
        ============
    ''', '''
             +-----+
             |     |
             O     |
            /|     |
                   |
                   |
        ============
    ''', '''
             +-----+
             |     |
             O     |
            /|\    |
                   |
                   |
        ============
    ''', '''
             +-----+
             |     |
             O     |
            /|\    |
            /      |
                   |
        ============
    ''', '''
             +-----+
             |     |
             O     |
            /|\    |
            / \    |
                   |
        ============
    '''
]

# variáveis que acomulam os chutes
certas, erradas = '', ''

# lista de nomes
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
nomes = requests.get(url).text.lower().split()


# ========================
# TODAS AS FUNÇÕES
# ========================

# retorna um nome sorteado da lista de nomes
def escolhe():
    nomeSorteado = choice(nomes)
    return nomeSorteado

# imprime o desenho da forca e as letras chutadas corretamente
def desenha():
    # verificando qual o estado na forca e imprimindo
    totalErros = len(erradas)
    print(forca[totalErros])

    # imprimindo letras corretas e faltantes
    for letra in nomeSorteado:
        print(letra, end=' ') if letra in certas else print('_', end=' ')

# recebe uma letra chutada e faz a consistencia de dados
def chute(letras):
    # solicitando uma letra
    chuteAtual = input('\n\nChute uma letra: ').lower()

	# verificando se a letra é válida
    while len(chuteAtual) > 1 \
        or chuteAtual == ' ' \
        or chuteAtual == '' \
        or chuteAtual in letrasChutadas \
        or chuteAtual in string.punctuation \
        or chuteAtual in string.digits:
            chuteAtual = input('Por favor, digite uma letra válida: ').lower()

    return chuteAtual

# verifica se o usuário deseja jogar novamente
def jogar_novamente():
    resposta = input('Deseja jogar novamente? (responda S/N): ').lower()
    
	# aceita apenas 's' e 'n' como resposta
    while resposta not in ['s', 'n']:
        resposta = input('Digite uma resposta válida (responda S/N): ').lower()
        
    return True if resposta == 's' else False
        
# verifica se o usuário ganhou
def ganhou():
    return set(certas) == set(nomeSorteado)


# ========================
# PROGRAMA PRINCIPAL
# ========================

# sorteando um nome
nomeSorteado = escolhe()

while True:
    # desenhando a forca
    desenha()

    # verificando as letras já chutadas
    letrasChutadas = certas + erradas

    # solicitando um chute(letra)
    chuteAtual = chute(letrasChutadas)

    # atualizando chutes corretos e errados
    if chuteAtual in nomeSorteado:
        certas += chuteAtual
    else:
        erradas += chuteAtual

    # verificando se é game over...
    if len(erradas) == len(forca):
        print(f'''
            ======================================
            GAME OVER! O nome era '{nomeSorteado}'
            ======================================
        ''')
		# verificando se o usuário deseja jogar novamente
        if jogar_novamente():
            certas, erradas = '', ''
            nomeSorteado = escolhe()
        else: break

    # ...ou se houve vitória
    elif ganhou():
        input(f'''
            ==============================================
            PARABÉNS! Você acertou o nome '{nomeSorteado}'
            ==============================================
        ''')
		# verificando se o usuário deseja jogar novamente
        if jogar_novamente():
            certas, erradas = '', ''
            nomeSorteado = escolhe()
        else: break