# 42.	O cardápio de uma lanchonete é o seguinte:
# a.	Especificação   Código  Preço
# b.	Cachorro Quente 100     R$ 1,20
# c.	Bauru Simples   101     R$ 1,30
# d.	Bauru com ovo   102     R$ 1,50
# e.	Hambúrguer      103     R$ 1,20
# f.	Cheeseburguer   104     R$ 1,30
# g.	Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
# por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
total = 0
while True:
    codigo = input('Código do produto: ')
    if codigo == '':
        break
    else:
        if codigo == '100':
            preco = 1.2
        if codigo == '101':
            preco = 1.3
        if codigo == '102':
            preco = 1.5
        if codigo == '103':
            preco = 1.2
        if codigo == '104':
            preco = 1.3
        if codigo == '105':
            preco = 1.0
        qtd = int(input('Quantidade do item: '))
        valor = qtd * preco
    total = total + valor
    print(f'{qtd} - R$  {preco:.2f} =R$ {valor:.2f}')
print(f'Total a pagar: R$ {total:.2f}')