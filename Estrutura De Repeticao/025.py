# 25.	Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
p = soma = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade == 0:
        break
    else:
        soma += idade
        p += 1
media = soma / p
if media <=25:
    turma = 'Jovem'
elif media < 60:
    turma = 'Adulta'
elif media >= 60:
    turma = 'Idosa'
print(f'Total de pessoas: {p}\n'
      f'Média de idade: {media}\n'
      f'Turma : {turma}')