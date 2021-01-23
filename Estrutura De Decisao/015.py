# 15.	Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
# triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# o	Dicas:
# o	Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# o	Triângulo Equilátero: três lados iguais;
# o	Triângulo Isósceles: quaisquer dois lados iguais;
# o	Triângulo Escaleno: três lados diferentes;
l1 = int(input('Digite lado 1: '))
l2 = int(input('Digite lado 2: '))
l3 = int(input('Digite lado 3: '))

if l1 == l2 == l3:
    print('Triângulo EQUILÁTERO.')
elif l1 != l2 != l3:
    print('Triângulo ESCALNO.')
else:
    print('Triângulo ISÓSCELES.')