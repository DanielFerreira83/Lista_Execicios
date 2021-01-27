# 3.	Faça um programa que leia e valide as seguintes informações:
# a.	Nome: maior que 3 caracteres;
# b.	Idade: entre 0 e 150;
# c.	Salário: maior que zero;
# d.	Sexo: 'f' ou 'm';
# e.	Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite nome: ')
while len(nome) < 3:
    nome = input('Nome curto, tente novamente: ')
idade = int(input('Digite idade: '))
while True:
    if 0 < idade and idade < 150:
        salario = float(input('Dgitie salário: '))
        break
    else:
        idade = int(input('Idade inválida. Digite idade: '))
while salario <= 0:
    salario = float(input('Salário deve ser maior que 0: '))

sexo = input('Dgitie SEXO - f - FEMININO ou m - MASCULINO:')
while sexo not in 'fm':
    sexo = input('Valor digitado inválido, tente novamente: ')
est_civil = input('Digite estado civil: s - SOLTEIRO, c - CASADO, v - VIÚVO, d - DIVORCIADO')
while est_civil not in 'scvd':
    est_civil = input('Valor invpalido, digite s - SOLTEIRO, c - CASADO, v - VIÚVO, d - DIVORCIADO')

print(f'{nome}, {idade}, {salario}, {sexo} e {est_civil}')