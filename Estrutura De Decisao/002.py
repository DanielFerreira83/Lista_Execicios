# 2.	Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def funcao():
    num = int(input('Dogite um número: '))
    if num < 0 :
        print(f'{num} é negativo')
    if num > 0:
        print(f'{num} é positivo')
    else:
        print(f'{num} não definido.')


if __name__ =='__main__':
    funcao()