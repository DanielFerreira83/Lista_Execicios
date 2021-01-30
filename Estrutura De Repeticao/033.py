# 33.	O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
soma = 0
c = 0
while True:
    temp = float(input('Temperatura em º Celcius: '))
    if temp != 0:
        c += 1
        if c == 1:
            menor = temp
            maior = temp
        else:
             if temp > maior:
                 maior = temp
             elif temp < menor:
                 menor = temp
        soma += temp
    else:
        break
media = soma / c
print(f'Menor temperatura: {menor}º Celcius\n'
      f'Maior temperatura: {maior}º Celcius\n'
      f'Média de temperaturas: {media:.2f}º Celcius.')