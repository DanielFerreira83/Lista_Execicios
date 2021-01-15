# 17.	Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
# de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# o	Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# o	comprar apenas latas de 18 litros;
# o	comprar apenas galões de 3,6 litros;
# o	misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.
from math import ceil
def loja():
    area = float(input('Digite aera a ser pintada em m²: ')) # 108

    litros = (area / 6) * 1.1
    latas = litros / 18
    galao = litros / 3.6

    preco_latas = round(latas+0.5) * 80
    preco_galao = round(galao+0.5) * 25

    print(f'{round(latas + 0.5)} latas , preço R$ {preco_latas:.2f}')
    print(f'{round(galao + 0.5)} galão , preço R$ {preco_galao:.2f}')
    max_lata = int(litros // 18)
    max_galao = round(((litros % 18) / galao)+0.5)
    melhor_preco = (max_lata * 80) + (max_galao * 25)
    print(f'{max_lata} latas e {max_galao} galão, preço R$ {melhor_preco:.2f}')


if __name__=='__main__':
    loja()
