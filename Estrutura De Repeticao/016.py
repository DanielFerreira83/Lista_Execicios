# 16.	A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série
# até que o valor seja maior que 500.
p1 = 0
p2 = 1
while p1 <= 500:
    print(p1, end= ' ')
    p = p1
    p1 = p2
    p2 = p + p2
