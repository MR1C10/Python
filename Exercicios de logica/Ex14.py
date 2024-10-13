"""
14 - Faça um algoritmo que receba um valor A e B, e troque o
valor de A por B e o valor de B por A e imprima na tela os valores.
"""

a=10
b=20

if a != b:
    armazenamento=a # armazena o valor de a(10)
    a=b # a recebe o valor de b(20)
    b=armazenamento # b recebe o valor de a(10) 

print("a=10", a)
print("b=20", b)

"""
a=10
b=20

if a != b:
    troca= False 
    
    while not troca:
        armazenamento=a # armazena o valor de a(10)
        a=b # a recebe o valor de b(20)
        b=armazenamento # b recebe o valor de a(10) 
        troca=True

print("a=10", a)
print("b=20", b)
"""