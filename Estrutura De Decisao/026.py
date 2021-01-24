# 26.	Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# o	Álcool:
# o	até 20 litros, desconto de 3% por litro
# o	acima de 20 litros, desconto de 5% por litro
# o	Gasolina:
# o	até 20 litros, desconto de 4% por litro
# o	acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
# combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
litros = int(input('Quantos LITROS vao colocar? '))
tipo = input('Digite o tipo de combustivel: A - alcool ou G - gasolina ')
if tipo in 'Aa':
    if litros <= 20:
        valor = (litros * 2.5)
        v_desc = valor - (valor*0.03)
    else:
        valor = (litros * 2.5)
        v_desc = valor - (valor * 0.05)
elif tipo in 'Gg':
    if litros <= 20:
        valor = (litros * 1.9)
        v_desc = valor - (valor*0.04)
    else:
        valor = (litros * 2.5)
        v_desc = valor - (valor * 0.06)

print(f'Por {litros} deverá ser pago com desconto R$ {v_desc:.2f}')