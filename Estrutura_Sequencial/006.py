# 6.	Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi

def circulo():
    raio = float(input('Digite um raio em metro de um círculo: '))
    area = pi * raio**2
    print(f'A áreaa de um círculo de raio {raio} metro é igual a {area:.2f} m².')


if __name__=='__main__':
    circulo()
