# 7.	Faça um programa que leia 5 números e informe o maior número.
n_maior = int(input('Número 1: '))
for n in range(4):
    num = int(input('Número 2: '))
    if num > n_maior:
        n_maior = num
print(f'O maior foi o {n_maior}.')