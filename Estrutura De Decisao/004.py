# 4.	Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def letra():
    letra = input('Digite uma letra:')
    if letra in 'aeiouAEIOU':
        print(f'{letra} é uma vogal.')
    else:
        print(f'{letra} é uma consoante.')


if __name__=='__main__':
    letra()