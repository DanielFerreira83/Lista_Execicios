# 19.	Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
#	Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
from random import randrange
soma = 0
for n in range(10):
    num = randrange(0, 100)
    if n == 0:
        menor = n
        maior = n
    else:
        if num > maior:
            maior = n
        elif num  < menor:
            menor = n
    soma += n
print(f'''
Menor = {menor}
Maior = {maior}
soma = {soma}
''')

