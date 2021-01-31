# 40.	Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
# valor dos juros, quantidade de parcelas e valor da parcela.
# a.	Os juros e a quantidade de parcelas seguem a tabela abaixo:
# b.	Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67
divida = float(input('Dívida: '))
print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
print(f'R$ {divida}           0               1                       R$ {divida} ')
tx = 0.10
for p in range(3,13,3):
    print(f'R$ {divida}           {tx * divida:.0f}             {p}                       R$ {(divida + (tx * divida)) / p:.2f} ')
    tx += 0.05