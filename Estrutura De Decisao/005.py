# 5.	Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# o	A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# o	A mensagem "Reprovado", se a média for menor do que sete;
# o	A mensagem "Aprovado com Distinção", se a média for igual a dez.
def media():
    nota1 = float(input('Digite nota 1: '))
    nota2 = float(input('Digite nota 2: '))
    media = (nota1+ nota2)/2
    if media >= 7:
        print(f'{media} - APROVADO')
    elif media < 7:
        print(f'{media} - REPROVADO')
    elif media == 10:
        print(f'{media} - APROVADO COM DISTINÇÃO')

if __name__ == '__main__':
    media()