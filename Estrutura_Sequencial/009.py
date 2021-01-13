# 9.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#o	C = 5 * ((F-32) / 9).
def temperatura():
    farenheint = float(input('Digite temperatura em Farenheit: '))
    celcius = 5 * ((farenheint-32) / 9)
    print(f'{farenheint:.1f} Farenheit é igual a {celcius:.1f}º Celcius.')



if __name__=='__main__':
    temperatura()
