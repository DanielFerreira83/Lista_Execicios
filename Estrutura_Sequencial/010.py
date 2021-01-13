# 10.	Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (C × 9/5) + 32

def temperatura():
    celcius = float(input('Digite temperatura em graus Celcius: '))
    fahrenheit = (celcius * 9/5) + 32
    print(f'{celcius:.1f}º Celcius equivale a {fahrenheit:.1f} Fahrenheit.')


if __name__ == '__main__':
    temperatura()