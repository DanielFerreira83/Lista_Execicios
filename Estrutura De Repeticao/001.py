# 1.	Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.
nota = float(input('Digite uma nota de 0 a 10: '))

while True:
    if 0 <= nota <= 10:
        print(f'Nota - {nota}')
        break
    else:
        nota = float(input('Nota inválida, digite nota válida e 0 a 10: '))
