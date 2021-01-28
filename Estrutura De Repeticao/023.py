#23.	Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão
# avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
n = int(input('Número: '))
cont  = c = 0
for j in range(1, n):
    for i in range(1, n):
        if j % i == 0:
            cont += 1
            c+=1
    if cont == 2:
        print(f'{j} é primo.')
    else:
        print(f'{j} não é primo.')
    cont = 0
print(f'Foi dividido {c} vezes;')