# 43.	Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
# utilizados são:
# a.	1 , 2, 3, 4  - Votos para os respectivos candidatos
# b.	(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# c.	5 - Voto Nulo
# d.	6 - Voto em Branco
# Faça um programa que calcule e mostre:
# e.	O total de votos para cada candidato;
# f.	O total de votos nulos;
# g.	O total de votos em branco;
# h.	A percentagem de votos nulos sobre o total de votos;
# i.	A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
total = joao = rita = hugo = jose = nulo = branco = 0
while True:
    voto = int(input('''1 - Ana
    2 - João
    3 - Rita
    4 - Hugo
    5 - José
    5 - Nulo
    6 - Branco
    '''))
    if voto == 0:
        break
    else:
        if voto == 1:
            joao += 1
        elif voto == 2:
            rita += 1
        elif voto == 3:
            hugo += 1
        elif voto == 4:
            jose += 1
        elif voto == 5:
            nulo += 1
        elif voto == 6:
            branco += 1
        total += 1
perc_nulo = total / nulo
perc_branco = total / branco
print(f'João   - {joao} votos\n'
      f'Rita   - {rita} votos\n'
      f'Hugo   - {hugo} votos\n'
      f'José   - {jose} votos\n'
      f'Nulo   - {nulo} votos\n'
      f'Branco - {branco} votos\n'
      f'Percentagem de Nulos - {perc_nulo}%\n'
      f'Percentual de Brancos - {perc_branco}%')