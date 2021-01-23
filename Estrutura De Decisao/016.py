# 16.	Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
# pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# o	Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os
# demais valores, sendo encerrado;
# o	Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# o	Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# o	Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
a = int(input('Digite valor de a: '))
if a == 0 :
    print('a sendo 0, não é equação do 2º grau.')
else:
    b = int(input('Digite valor de b: '))
    c = int(input('Digite valor de c: '))
    delta = (b**2) - 4 * a * c
    if delta < 0:
        print('Equação não tem raizes reais.')
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / 2*a
        print(f'A raiz da qeuação é {x}')
    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print(f'''
        a = {a}
        b = {b}
        c = {c}
        {a}x² + {b}x - {c} = 0
        As raízes da equação é:
        Raiz 1 = {x1}
        Raiz 2 = {x2}
''')

