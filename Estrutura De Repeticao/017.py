# 17.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input('Digite um Fatorial: '))
fat = 1
print(f'{num}! = ', end=' ')
for n in range(num, 0, -1):
    fat = fat * n

    print(f'{n}'+'.', end=' ')

print(f'= {fat}')