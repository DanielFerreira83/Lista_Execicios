# 28.	O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
# o	                      Até 5 Kg           Acima de 5 Kg
# o	File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# o	Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# o	Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
# pagamento, valor do desconto e valor a pagar.
print('''
1 - File Duplo
2 -	Alcatra
3 -	Picanha
''')
tipo1 = int(input('Escolha [ 1 - 2 - 3 ] para tipode carne: '))
qtd1 = int(input('Escolha quantidade em KG do tipo escolhido: '))

if tipo1 == 1 and qtd1 <= 5:
    tipo1 = 'File Duplo'
    preco1 = qtd1 * 4.9
elif tipo1 == 1 and qtd1 > 5:
    tipo1 = 'File Duplo'
    preco1 = qtd1 * 5.8
if tipo1 == 2 and qtd1 <= 5:
    tipo1 = 'Alcatra'
    preco1 = qtd1 * 5.9
elif tipo1 == 2 and qtd1 > 5:
    tipo1 = 'Alcatra'
    preco1 = qtd1 * 6.8
if tipo1 == 3 and qtd1 <= 5:
    tipo1 = 'Picanha'
    preco1 = qtd1 * 6.9
elif tipo1 == 3 and qtd1 > 5:
    tipo1 = 'Picanha'
    preco1 = qtd1 * 7.8
tipo2 = int(input('Escolha [ 1 - 2 - 3 ] para tipode carne: '))
qtd2 = int(input('Escolha quantidade em KG do tipo escolhido: '))
if tipo2 == 1 and qtd2 <= 5:
    tipo2 = 'File Duplo'
    preco2 = qtd1 * 4.9
elif tipo2 == 1 and qtd2 > 5:
    tipo2 = 'File Duplo'
    preco2 = qtd2 * 5.8
if tipo2 == 2 and qtd2 <= 5:
    tipo2 = 'Alcatra'
    preco2 = qtd2 * 5.9
elif tipo2 == 2 and qtd2 > 5:
    tipo2 = 'Alcatra'
    preco2 = qtd2 * 6.8
if tipo2 == 3 and qtd2 <= 5:
    tipo2 = 'Picanha'
    preco2 = qtd1 * 6.9
elif tipo2 == 3 and qtd2 > 5:
    tipo2 = 'Picanha'
    preco2 = qtd2 * 7.8

preco = preco1 + preco2
forma = input('Pagar com cartao TABAJARA? ')
if forma in 'sim':
    preco = preco - (preco * 0.05)
print(f''''
{"Hipermercado Tabajara":^40}
{"-"*40}
{qtd1} Kg {tipo1} {preco1:>30.2f}
{qtd2} Kg {tipo2} {preco2:>30.2f}
Total {preco:>32.2f}
''')