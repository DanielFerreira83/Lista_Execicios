# 39.	Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
# obtidos os seguintes dados:
# a.	Código da cidade;
# b.	Número de veículos de passeio (em 1999);
# c.	Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d.	Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e.	Qual a média de veículos nas cinco cidades juntas;
# f.	Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio
maior_indice = 0
menor_indice = 0
soma_veiculo = 0
soma_acidente = 0

for i in range(5):
    cidade = int(input('Código da cidade: '))
    veiculo = int(input('Número de veículos: '))
    acidente = int(input('Número de acidentes: '))
    indice = veiculo // acidente
    if i == 0:
        maior_indice = indice
        menor_indice = indice
        cd_cidade_maior = cidade
        cd_cidade_menor = cidade
    if indice < menor_indice:
        menor_indice = indice
        cd_cidade_menor = cidade
    elif indice > maior_indice:
        maior_indice = indice
        cd_cidade_maior = cidade
    soma_veiculo += veiculo
    soma_acidente += acidente
media_veiculo = soma_veiculo / 5
media_acidente = soma_acidente / 5
print(f'Maior índice de acidentes {maior_indice} da cidade {cd_cidade_maior}\n'
      f'Menor indice de acidente {menor_indice} da cidade {cd_cidade_menor}\n'
      f'Média de veículos: {media_veiculo:.0f} por cidade\n'
      f'Média de acidentes: {media_acidente:.0f} por cidade')