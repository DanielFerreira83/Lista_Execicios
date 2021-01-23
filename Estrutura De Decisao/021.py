# 21.	Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois 
# informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas 
# existentes na máquina.
# o	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 
# 5 e uma nota de 1;
# o	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas 
# de 10, uma nota de 5 e quatro notas de 1.
valor = int(input('Digite quanto quer sacar R$ : '))
if 10 <= valor <=600:
    if valor > 99:
        n100 = valor // 100
        valor = valor % 100
        print(f'{n100} notas de R$ 100')
    if valor > 49:
        n50 = valor // 50
        valor = valor % 50
        print(f'{n50} notas de R$ 50')
    if valor > 9:
        n10 = valor // 10
        valor = valor % 10
        print(f'{n10} notas de R$ 10')
    if valor > 4:
        n5 = valor // 5
        valor = valor % 5
        print(f'{n5} notas de R$ 5')
        print(f'{valor} notas de R$ 1')
else:
    print('Valor abaixo do permitido.')