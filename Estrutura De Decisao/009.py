# 9.	Faça um Programa que leia três números e mostre-os em ordem decrescente.
def crescente():
    n1 = int(input('Nùmero 1: '))
    n2 = int(input('Número 2: '))
    n3 = int(input('Número 3: '))

    if n2 < n1 > n3 and n2 > n3:
        print(f'{n1} > {n2} > {n3}.')
    elif n1 < n2 > n3 and n1 > n3:
        print(f'{n2} > {n1} > {n3}.')
    elif n1 < n2 > n3 and n3 > n1:
        print(f'{n2} > {n3} > {n1}.')
    elif n1 < n3 > n2 and n1 > n2:
        print(f'{n3} > {n1} > {n2}.')
    elif n2 < n1 > n3 and n3 > n2:
        print(f'{n1} > {n3} > {n2}.')
    elif n1 < n3 > n2 and n2 > n1:
        print(f'{n3} > {n2} > {n1}.')


if __name__=='__main__':
    crescente()