# 11.	Altere o programa anterior para mostrar no final a soma dos números.
# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
# por eles.
num1 = int(input('Digite número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    num1, num2 = num2, num1
soma = 0
for n in range(num1+1, num2):
    soma += n
    print(n)
print(f'A Soma dos número é {soma}.')