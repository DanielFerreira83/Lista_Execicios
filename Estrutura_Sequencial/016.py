# 16.	Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
# de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
from math import ceil
def loja():
    area = float(input('Digite o tamanho em m²: '))
    valor = 80
    area_lata = 18 * 3
    qtd = ceil(area / area_lata)
    preco = qtd * valor
    print(f'A Qtd de latas usadas será {qtd:.0f} e o valor gasto é R$ {preco:.2f}')


if __name__=='__main__':
    loja()