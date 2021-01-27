# 14.	Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
# números impares.
cont_inpar = 0
cont_par = 0
for n in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        cont_par += 1
    if num % 2 != 0:
        cont_inpar += 1
print(f'''
{cont_par} números pares.
{cont_inpar} números inpares.''')