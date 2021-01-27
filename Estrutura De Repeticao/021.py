# 21.	Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é
# aquele que é divisível somente por ele mesmo e por 1.
from random import randint
primo = randint(0,50)
cont = 0
for n in range(1, primo+ 1):
    if primo % n == 0:
        cont += 1

if cont == 2:
    print(f'{primo} é PRIMO.')
else:
    print(f'{primo} nao é PRIMO.')