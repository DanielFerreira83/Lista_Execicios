# 10.	Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
# N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def turno():
    turno = input('Digite o turno que estuda [M-matutino ou V-Vespertino ou N- Noturno]')
    if turno in 'Mm':
        print('Boa dia!')
    elif turno in 'Vv':
        print('Boa tarde!')
    elif turno in 'Nn':
        print('Boa noite!')
    else:
        print('Valor Inválido!')


if __name__=='__main__':
    turno()
