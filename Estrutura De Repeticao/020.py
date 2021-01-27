# 20.	Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.
while True:
    num = int(input('Digite um Fatorial: '))
    if num > 0 and num < 16:
        fat = 1
        print(f'{num}! = ', end=' ')
        for n in range(num, 0, -1):
            fat = fat * n

            print(f'{n}'+'.', end=' ')

        print(f'= {fat}')
        cont = input('Quer continuar? ')
        if cont not in 'sim':
            break
    else:
        print('Número ora de intervalo limite.')