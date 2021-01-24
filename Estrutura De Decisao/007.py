# 7.	Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
if n2 < n1 > n3:
    print(f'{n1} é o maior')
elif n1 < n2 > n3:
    print(f'{n2} é o maior')
elif n2 < n3 > n1:
    print(f'{n3} é o maior')
if n2 > n1 < n3:
    print(f'{n1} é o mmenor')
elif n1 > n2 < n3:
    print(f'{n2} é o menor')
elif n1 > n3 < n2:
    print(f'{n3} é o menor')
