# GIOVANA THAÍS DE OLIVEIRA SILVA (DSM)

# importando bibliotecas necessárias
import requests
from random import choice

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

# inicializando variáveis que acomulam os chutes
certas, erradas = '', ''

# Fazendo a leitura da lista de nomes
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
nomes = requests.get(url).text.lower().split

# FUNÇÃO ESCOLHE: retorna um nome sorteado da lista de nomes
def escolhe():
    nomeSorteado = choice(nomes)
    return nomeSorteado

# FUNÇÃO DESENHA: imprime o desenho da forca e as letras chutadas corretamente
def desenha():
    # verificando qual o estado na forca e imprimindo
    totalErros = len(erradas)
    print(forca[totalErros])
    # verificando chutes corretos e imprimindo
    






