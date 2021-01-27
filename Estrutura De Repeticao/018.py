# 18.	Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
c = (8,6,2,3,4,9,1,7)
soma = 0
for i in range(0, len(c)):
    if i == 0 :
        maior = c[0]
        menor = c[0]
    if c[i] > maior:
        maior = c[i]
    if c[i] < menor:
        menor = c[i]
    soma += c[i]

print(f'''
Menor = {menor}
Maior = {maior}
Soma = {soma}
''')