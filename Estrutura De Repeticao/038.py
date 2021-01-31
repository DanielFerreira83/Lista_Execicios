# 38.	Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
# alto e o número do aluno mais baixo, junto com suas alturas.
altura_maior = 0
altura_menor = 0
for i in range(10):
    aluno = int(input('Aluno: '))
    altura = int(input('Altura: '))
    if i == 0:
        num_aluno_maior = aluno
        num_aluno_menor = aluno
        altura_maior = altura
        altura_menor = altura
    if altura > altura_maior:
        num_aluno_maior = aluno
        altura_maior = altura
    if altura < altura_menor:
        num_aluno_menor = aluno
        altura_menor = altura

print(f'Aluno mais alto: Aluno {num_aluno_maior} com {altura_maior} cm\n'
      f'Aluno mais baixo: Aluno {num_aluno_menor} com {altura_menor} cm')