# 19.	Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# o	Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# o	326 = 3 centenas, 2 dezenas e 6 unidades
# o	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
num = input('Digite um número menor que 1000: ')
centena = num[-3]
dezena = num[-2]
unidade = num[-1]
if len(num) == 1:
    print(f'{num} = {unidade} unidades')
elif len(num) == 2:
    print(f'{num} = {dezena} dezenas e {unidade} unidades')
elif len(num) == 3:
    print(f'{num} = {centena} centenas, {dezena} dezenas e {unidade} unidades')
