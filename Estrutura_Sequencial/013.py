# 13.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# o	Para homens: (72.7*h) - 58
# o	Para mulheres: (62.1*h) - 44.7
def peso():
    altura = float(input('Digite altura de uma pessoa: '))
    homem = (72.7 * altura) - 58
    mulher = (62.1 * altura) - 44.7
    print(f'Tendo {altura} m, o peso ideal pra homem é {homem:.2f} kg e para mulher é {mulher:.2f} kg.')


if __name__=='__main__':
    peso()
