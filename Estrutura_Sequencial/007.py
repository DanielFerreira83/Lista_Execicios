# 7.	Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def quadrado():
    num = int(input('Digite o lado de um quadrado: '))
    area = num **2
    d_area = area * 2
    print(f'Um quadrado de lado {num}, tem de área {area}, seu dobro é {d_area}.')


if __name__=='__main__':
    quadrado()