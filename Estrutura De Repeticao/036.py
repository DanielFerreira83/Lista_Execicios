# 36.	Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e
# o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua
# altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais
# gordo e do mais magro, além da média das alturas e dos pesos dos clientes
soma_peso = 0
soma_altura = 0
maior_altura = 0
menor_altura = 0
maior_peso = 0
menor_peso = 0
cont = 0
while True:
    codigo = int(input('Código: '))
    if codigo == 0:
        break
    else:
        altura = int(input('Altura (cm): '))
        peso = int(input('Peso (kg): '))
        cont += 1
        if cont == 1:
            maior_altura = altura
            cd_maior_altura = codigo
            menor_altura = altura
            cd_menor_altura = codigo
            maior_peso = peso
            cd_maior_peso = codigo
            menor_peso = peso
            cd_menor_peso = codigo
        if altura > maior_altura:
            maior_altura = altura
            cd_maior_altura = codigo
        elif altura < menor_altura:
            menor_altura = altura
            cd_menor_altura = codigo
        if peso > maior_peso:
            maior_peso = peso
            cd_maior_peso = codigo
        elif peso < menor_peso:
            menor_peso = peso
            cd_menor_peso = codigo
        print('-'* 40)
        soma_altura += altura
        soma_peso += peso
media_altura = soma_altura / cont
media_peso = soma_peso / cont
print(f'Maior altura: código {cd_maior_altura} com {maior_altura} cm\n'
      f'Menor altura: código {cd_menor_altura} com {menor_altura} cn\n'
      f'Maior peso: código {cd_maior_peso} com {maior_peso} kg\n'
      f'Menor peso: código {cd_menor_peso} com {menor_peso} kg\n'
      f'Média de altura: {media_altura:.2f}\n'
      f'Média peso: {media_peso:.3f} kg')