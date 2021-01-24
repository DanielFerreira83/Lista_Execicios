# 6.	Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('Núemro 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
if n2 < n1 >n3:
    print(f'{n1} é o maior número.')
elif n1 < n2 > n3:
    print(f'{n2} é o maior número.')
elif n1 < n3 > n2:
    print(f'{n3} é o maior númeero.')
