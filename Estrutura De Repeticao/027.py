# 27.	Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
qtd_alunos = 0
cont = 1
turma = int(input('Quantidade de turma: '))
while cont <= turma:
    alunos = int(input(f'Quantidade de alunos {cont}: '))
    if alunos < 40:
        cont +=1
        qtd_alunos+= alunos


media = qtd_alunos / turma
print(f'Em {turma} tem {media} em média por turma.')