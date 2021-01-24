# 25.	Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# o	"Telefonou para a vítima?"
# o	"Esteve no local do crime?"
# o	"Mora perto da vítima?"
# o	"Devia para a vítima?"
# o	"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
p1 = input("Telefonou  para a vítima [ sim - nao ]: ")
p2 = input('Esteve no local do crime? [ sim - nao ]: ')
p3 = input('Mora perto da vítima? [ sim - nao ]: ')
p4 = input('Devia para a vítima? [ sim - nao ]: ')
p5 = input('Já trabalhou com a vítima? [ sim - nao ]: ')

cont = 0
if p1 == 'sim':
    cont += 1
if p2 == 'sim':
    cont += 1
if p3 == 'sim':
    cont += 1
if p4 == 'sim':
    cont += 1
if p5 == 'sim':
    cont += 1
if cont == 2:
    print('Suspeito!')
elif 3 <= cont <= 4:
    print('Cumplica!')
elif cont == 5:
    print('Assassino!')
else:
    print('Inocente!')