# 1.	Faça um Programa que peça dois números e imprima o maior deles.
def maior():
    num1 = int(input('Digite um npumero: '))
    num2 = int(input('Digite outro número: '))
    if num1 > num2:
        print(f'O maior número é {num1}.')
    else:
        print(f'O maior número é {num2}')

if __name__=='__main__':
    maior()