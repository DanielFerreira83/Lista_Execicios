# 34.	Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo
# é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele
# é ou não um número primo.
num = int(input('Verifica primo: '))
i = 2
while i < num:
    if num % i == 0:
        print(f'{num} não é primo.')
        break
    elif i == num-1:
        print(f'{num} é primo.')
    i += 1

