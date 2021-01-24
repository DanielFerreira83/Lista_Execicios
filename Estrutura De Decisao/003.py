# 3.	Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.

sexo = input('Digite M - para masculino e F para feminino: ')
if sexo in "Mm":
    print(f'Sexo Masculino.')
elif sexo in "fF":
    print(('Sexo Feminino.'))
else:
    print('Não identificado.')
