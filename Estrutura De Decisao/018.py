# 18.	Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input('Digite uma data ( dd/mm/aaaa ): ')
dia = data[:2]
mes = data[3:5]
ano = data[6:]
if 0 < int(dia) <= 31 and 0 < int(mes) <= 12 and int(ano) > 0:
    print(f'{data} é uma data válida.')
