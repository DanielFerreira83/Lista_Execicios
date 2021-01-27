# 5.5.	Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.
paisA = int(input('População do país A: '))
txA = float(input('Taxa de crescimento da pais A'))
paisB = int(input('População do país B: '))
txB = float(input('Taxa de crescimento da pais A'))
ano = 0
while paisA < paisB:
    paisA = paisA + (paisA * txA)
    paisB = paisB + (paisB * txB)
    ano = ano + 1

print(f'{ano} para que Pais A ultrapasse o Pais B.')