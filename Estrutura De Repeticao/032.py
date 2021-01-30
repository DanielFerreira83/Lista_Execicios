# 32.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:
# a.	Fatorial de: 5
# b.	5! =  5 . 4 . 3 . 2 . 1 = 120
fatorial = int(input('Fatorial de: '))
print(f'{fatorial}! = ', end='')
fat = 1
for i in range(fatorial, 0,-1):
    print(f'{i}', end='')
    if i != 1:
        print('.',end='')
    else:
        print('=',end=' ')
    fat = fat * i
print(f'{fat}')
