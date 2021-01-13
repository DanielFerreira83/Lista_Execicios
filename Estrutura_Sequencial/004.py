# 4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def media():
    n1 = float(input('Digite primeira nota: '))
    n2 = float(input('Digite segunda nota: '))
    n3 = float(input('Digite terceira nota: '))
    n4 = float(input('Digite quarta: '))
    media = (n1 + n2 + n3 + n4)/4
    print(f'A média das notas {n1}, {n2}, {n3} e {n4} é {media:.2f}')


if __name__ == '__main__':
    media()