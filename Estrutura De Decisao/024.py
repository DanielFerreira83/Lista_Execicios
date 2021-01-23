# 24.	Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O
# resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# o	par ou ímpar;
# o	positivo ou negativo;
# o	inteiro ou decimal.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
operacao = input('Qual operação deseja resolver [ + , - , / , * ]')

if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '/':
    resultado = n1 / n2
elif operacao == '*':
    resultado = n1 * n2

if resultado % 2 == 0:
    print(f'{resultado} é PAR.')
else:
    print(f'{resultado} é ÍMPAR.')

if resultado > 0:
    print(f'{resultado} é POSITOVO.')
elif resultado < 0:
    print(f'{resultado} é NEGATIVO.')

if resultado == round(resultado):
    print(f'{resultado} é INTEIRO.')
elif resultado != round(resultado):
    print(f'{resultado} é DECIMAL..')