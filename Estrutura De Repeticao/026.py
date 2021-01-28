# 26.	Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
# eleitor votar e ao final mostrar o número de votos de cada candidato.
va = vb = vc = 0
e = int(input('Total de eleitores: '))
for n in range(e):
    voto = input('A - Alberto\n'
                 'B - Bruno\n'
                 'C - Carlos')
    if voto in 'Aa':
        va += 1
    elif voto in'Bb':
        vb += 1
    elif voto in 'Cc':
        vc += 1
print(f'Alberto teve - {va}\n'
      f'Bruno teve - {vb}\n'
      f'Carlos  teve - {vc}')