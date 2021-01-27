# 8.	Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for n in range(5):
    num = int(input(f'{n+1} número: '))
    soma = soma + num
media = soma / 5
print(f'Soma dos números {soma} e sua média {media}.')