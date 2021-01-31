# 41.	Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
# seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
cont1 = cont2 = cont3 = cont4 = 0
while True:
    num = int(input('Digite número: '))
    if num < 0:
        break
    else:
        if num >= 0 and num <= 25:
            cont1 += 1
        if num >= 26 and num <= 50:
            cont2 += 1
        if num >= 51 and num <= 75:
            cont3 += 1
        if num >= 76 and num <= 100:
            cont4 += 1
print(f'[0-25] - {cont1}\n'
      f'[26-50] - {cont2}\n'
      f'[51-75] - {cont3}\n'
      f'[76-100] - {cont4}\n')