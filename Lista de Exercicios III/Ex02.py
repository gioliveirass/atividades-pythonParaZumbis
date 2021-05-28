# Exercicio 02
print('Exercicio 02')
usuario = input('Usuário: ')
senha = input('Senha: ')
while usuario == senha:
    print('Usuário e senha não podem ter o mesmo valor! Cadastre-se novamente:')
    usuario = input('Usuário: ')
    senha = input('Senha: ')
print('Usuário e senha cadastrados com sucesso.')