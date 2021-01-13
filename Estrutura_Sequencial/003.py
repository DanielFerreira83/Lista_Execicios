# 3.	Faça um Programa que peça dois números e imprima a soma.
def soma():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    soma = num1 + num2
    print(f'A soma de {num1} e {num2} é {soma}.')


if __name__== '__main__':
    soma()