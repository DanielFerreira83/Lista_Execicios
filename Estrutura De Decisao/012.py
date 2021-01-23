# 12.	Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# o	Desconto do IR:
# o	Salário Bruto até 900 (inclusive) - isento
# o	Salário Bruto até 1500 (inclusive) - desconto de 5%
# o	Salário Bruto até 2500 (inclusive) - desconto de 10%
# o	Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# o	        Salário Bruto: (5 * 220)        : R$ 1100,00
# o	        (-) IR (5%)                     : R$   55,00
# o	        (-) INSS ( 10%)                 : R$  110,00
# o	        FGTS (11%)                      : R$  121,00
# o	        Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00
def folha():
    sal_hora = float(input('Valor da hora trabalhada: '))
    hora = int(input('Hora trabalhada no mês: '))
    salario = sal_hora * hora
    if salario <= 900:
        sal_bruto = salario
    elif salario <= 1500:
        ir = salario * 0.05
        inss = salario * 0.1
        fgts = salario * 0.11
        desconto = ir + inss + fgts
    elif salario <= 2500:
        ir = salario * 0.1
        inss = salario * 0.1
        fgts = salario * 0.11
        desconto = ir + inss + fgts
    elif salario > 2500:
        ir = salario * 0.2
        inss = salario * 0.1
        fgts = salario * 0.11
        desconto = ir + inss + fgts

    print(f'''
    Salario Bruto R$        {salario:.2f}
    (-) IR R$               {ir:.2f}
    (-) INSS R$             {inss:.2f}
    FGTS (11%) R$           {fgts:.2f}
    Total desconto R$       {desconto:.2f}
    Salário líquido R$      {salario - desconto:.2f}''')


if __name__== '__main__':
    folha()