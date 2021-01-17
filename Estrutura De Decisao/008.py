# 8.	Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.
def preco():
    p1 = float(input('Preço 1: '))
    p2 = float(input('Preço 2: '))
    p3 = float(input('Preço 3: '))
    if p2 > p1 < p3:
        print(f'O produto 1 tem o preço menor - R$ {p1}.')
    elif p1 > p2 < p3:
        print(f'O produto 2 tem o preço menor - R$ {p2}.')
    if p2 > p3 < p1:
        print(f'O produto 3 tem o preço menor - R$ {p3}.')


if __name__ == '__main__':
    preco()