# 12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando
# a seguinte fórmula: (72.7*altura) - 58
def peso():
    altura = float(input('Digite a altura de uma pessoa: '))
    peso = (72.7 * altura) - 58
    print(f'O peso ideal é {peso:.2f} kg')


if __name__ =='__main__':
    peso()