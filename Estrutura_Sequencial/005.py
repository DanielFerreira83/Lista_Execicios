# 5.	Faça um Programa que converta metros para centímetros.
def converte():
    num = float(input('Digite um número para converter de metro para centímetro: '))
    conv = num * 100
    print(f'{num:.0f} metro é o mesmo que {conv:.0f} centímetros.')


if __name__=='__main__':
    converte()
