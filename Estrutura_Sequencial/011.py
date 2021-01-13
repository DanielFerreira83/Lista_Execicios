# 11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o	o produto do dobro do primeiro com metade do segundo .
# o	a soma do triplo do primeiro com o terceiro.
# o	o terceiro elevado ao cubo.
def funcao():
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite outro número inteiro: '))
    num3 = float(input('Digite um número real: '))
    produto = (num1*2) + (num2/2)
    soma = (num1 * 3) + num3
    cubo = num3**3
    print(f'O dobro de {num1} com a metade de {num2} é {produto:.1f}.')
    print(f'A soma do triplo de {num1} com {num3:.1f} é {soma:.1f}.')
    print(f'O cubo de {num3:1f} é {cubo:.1f}.')


if __name__=='__main__':
    funcao()