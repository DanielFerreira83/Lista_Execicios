# 44.	Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar
# ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e
# a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# a.	Maior e Menor Acerto;
# b.	Total de Alunos que utilizaram o sistema;
# c.	A Média das Notas da Turma.
# Gabarito da Prova:
#
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
# alunos usarem o programa.
# gabarito
q1 = 'A'
q2 = 'B'
q3 = 'C'
q4 = 'D'
q5 = 'E'
q6 = 'E'
q7 = 'D'
q8 = 'C'
q9 = 'B'
q10 = 'A'
nota = 0
for q in range(1,11):
    r = input(f'Questão {q}: ')
    if q == 1:
        if r == q1:
            nota += 1
    if q == 2:
        if r == q2:
            nota += 1
    if q == 3:
        if r == q3:
            nota += 1
    if q == 4:
        if r == q4:
            nota += 1
    if q == 5:
        if r == q5:
            nota += 1
    if q == 6:
        if r == q6:
            nota += 1
    if q == 7:
        if r == q7:
            nota += 1
    if q == 8:
        if r == q8:
            nota += 1
    if q == 9:
        if r == q9:
            nota += 1
    if q == 10:
        if r == q10:
            nota += 1
print(f'Alino tirou nota - {nota}')