# 24.	Faça um programa que calcule o mostre a média aritmética de N notas.
c = 0
soma = 0
while True:
    num = int(input('Número: '))
    soma += num
    c += 1
    p = input('Quer continuar? ')
    if p in 'nao':
        break

media = soma / c
print(f'A média é {media}')