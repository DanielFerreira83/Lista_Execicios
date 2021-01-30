# 28.	Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
# gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
qtd_cd = int(input('Quantidade de CD: '))
soma= 0
for cd in range(qtd_cd):
    preco = float(input(f'Preço do CD {cd}: '))
    soma += preco
media = soma / qtd_cd
print(f'em {qtd_cd} CDs foi gasto em média R$ {media:.2f}')
