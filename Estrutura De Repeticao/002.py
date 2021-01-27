# 2.	Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = input('Digite usuário: ')
senha = input('Digite a senha: ')
while usuario == senha:
    senha = input('Senha não pode ser igual usuário, tente novamente: ')
print('Login confirmado.')