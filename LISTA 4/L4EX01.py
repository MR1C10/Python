"""
1.Desenvolva um algoritmo (fluxograma e pseudocódigo) que leia dois  números e 
mostre o menor.

"""

x= int(input("digite um numero:"))
y= int(input("digite um numero:"))
z= int(input("digite um numero:"))
if(x==y):
    print("os numeros são iguais")
else:
    if(x<y):
        print("o numero menor é",x)
    else:
        print("o numero menor é",y)   
