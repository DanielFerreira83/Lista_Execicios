# 15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
# mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para
# o INSS e 5% para o sindicato, faça um programa que nos dê:
# o	salário bruto.
# o	quanto pagou ao INSS.
# o	quanto pagou ao sindicato.
# o	o salário líquido.
# o	calcule os descontos e o salário líquido, conforme a tabela abaixo:
# o	+ Salário Bruto : R$
# o	- IR (11%) : R$
# o	- INSS (8%) : R$
# o	- Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

def programa():
    valorHora = float(input('Digite o valor por hora de trabalho: '))
    horaMes = int(input('Digite hora por mês: '))
    salario = valorHora * horaMes
    ir = (salario * 0.11)
    inss = (salario * 0.08)
    sindicato = (salario * 0.05)
    print(f'''+ Salário Bruto : R$ {salario:.2f}
                + IR (11%) : R$ {ir:.2f}
                - INSS (8%) : R$ {inss:.2f} 
                - Sindicato (5%) : R$ {sindicato:.2f}
                + Salário Líquido : R$ {salario - ir - inss - sindicato:.2f}''')


if __name__=='__main__':
    programa()