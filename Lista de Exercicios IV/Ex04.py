# Exercicio 04
print('Exercicio 04')
import random
resultado = []
statement = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
statement = statement.replace(',', '')
statement = statement.replace('.', '')
statement = statement.replace(':', '')
statement = statement.lower()
statement = statement.split()
for x in statement:
    if x[0] in 'python' or x[-1] in 'python':
        resultado.append(x)
print(resultado)