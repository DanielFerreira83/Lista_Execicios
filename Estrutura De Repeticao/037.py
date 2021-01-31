# 37.	Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# a.	Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# b.	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# c.	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que
# o usuário digite o salário inicial do funcionário.
ano = 1995
salario = 1000
atual = 2021
taxa = 0.015
while ano < atual:
    ano = ano + 1
    if ano == 1996:
        aumento = salario * taxa
        salario = salario + aumento
    else:
        aumento *= 2
        salario = salario + aumento

print(f'Em {ano} o salário será R$ {salario:.2f}')