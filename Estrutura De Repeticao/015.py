# 15.	A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
# série até o n−ésimo termo.
p1 = 1
p2 = 1
while p1 < 100:
    print(f'{p1}')
    p = p1
    p1 = p2
    p2 = p + p2
