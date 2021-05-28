# Exercicio 05
print('Exercicio 05')
import random
resultado = 0
statement = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
statement = statement.replace(',', '')
statement = statement.replace('.', '')
statement = statement.replace(':', '')
statement = statement.lower()
statement = statement.split()
def caracteresPy(palavra):
    for caractere in palavra: # Para cada caractere da palavra...
        if caractere in 'python': # Verifica se o caractere está em 'python'
            return True # retorna verdadeiro se o caractere estiver em 'python'
    return False # retorna falso se o caractere não estiver em 'python'
for x in statement:
    if caracteresPy(x) and len(x) > 4: # passa x como parametro
        resultado = resultado + 1
print(f'Palavras que possuem uma das letras "python" e com mais de 4 caracteres: {resultado}.')