# 45.	Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de
# cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
# a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média).
# Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
# O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
#
# Resultado final:
# Rodrigo Curvêllo: 5.9 m
saltos = 0
for s in range(1,6):
    salto = float(input(f'Salto {s}: '))
    if s == 1:
        s1 = salto
        melhor = salto
        pior = salto
    elif s == 2:
        s2 = salto
        if salto > melhor:
            melhor = salto
        elif salto < pior:
            pior = salto
    elif s == 3:
        s3 = salto
        if salto > melhor:
            melhor = salto
        elif salto < pior:
            pior = salto
    elif s == 4:
        s4 = salto
        if salto > melhor:
            melhor = salto
        elif salto < pior:
            pior = salto
    elif s == 5:
        s5 = salto
        if salto > melhor:
            melhor = salto
        elif salto < pior:
            pior = salto
    saltos += salto
exclusao = melhor + pior
media = (saltos - exclusao) / 3
print(f'Atleta: Rodrigo Curvêllo\n'
      f'Primeiro Salto: {s1} m\n'
      f'Segundo Salto: {s2} m\n'
      f'Terceiro Salto: {s3} m\n'
      f'Quarto Salto: {s4} m\n'
      f'Quinto Salto: {s5} m\n'
      f'\n'
      f'Melhor salto:  {melhor} m\n'
      f'Por salto: {pior} m\n'
      f'Média dos demais saltos: {media:.1f} m\n'
      f'\n'
      f'Resultado final:\n'
      f'Rodrigo Curvêllo: {media:.1f} m')