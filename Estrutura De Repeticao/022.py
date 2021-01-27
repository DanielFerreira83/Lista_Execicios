# 22.	Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele
# é divisível.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é
# aquele que é divisível somente por ele mesmo e por 1.
from random import randint
primo = randint(0,50)
cont = 0
if primo == 0 or primo == 1:
    cont = 1
else:
    for n in range(2, primo):
        if primo % n == 0:
            cont += 1
            print(f'{n}')

if cont == 0:
    print(f'{primo} é PRIMO.')
else:
    print(f'{primo} nao é PRIMO.')
