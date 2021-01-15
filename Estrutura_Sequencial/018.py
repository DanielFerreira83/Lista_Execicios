# 18.	Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
def internet():
    tamanho = int(input('Digite o tanhanho do arquivo em Mb: '))
    velocidade = int(input('Digite a velocidade da internet em MBs: '))
    tempo = (tamanho / velocidade) / 60
    print(f'Um arquivo com {tamanho} Mb com internet de {velocidade} MBs, demora {tempo:.2f} minutos.')

if __name__=='__main__':
    internet()