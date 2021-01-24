# 27.	Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# o	                      Até 5 Kg           Acima de 5 Kg
# o	Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# o	Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
# de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
# adquiridas e escreva o valor a ser pago pelo cliente.

kilo_maca = float(input('Quantos quilos de maçâ? '))
kilo_morango = float(input('Quantos quilos morango? '))
if kilo_maca <= 5:
    preco_maca = kilo_maca * 1.8
else:
    preco_maca = kilo_maca * 1.5
if kilo_morango <= 5:
    preco_morango = kilo_morango * 2.5
else:
    preco_morango = kilo_morango * 2.2
valor = preco_morango + preco_maca
if valor > 25 or kilo_maca + kilo_morango == 8:
    valor = valor - (valor * 0.1)

print(f'{kilo_maca} de maçãs e {kilo_morango} de morango, custam R$ {valor}.')