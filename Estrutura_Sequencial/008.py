# 8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
# mostre o total do seu salário no referido mês.
def salario():
    sal_hora = float(input('Digite quando ganha por hora: '))
    hora = int(input('Digite hora trabalhas por mês: '))
    salario = sal_hora * hora
    print(f'O salária de quem trabalha {hora} horas por mês é, R$ {salario:.2f}')


if __name__ == "__main__":
    salario()