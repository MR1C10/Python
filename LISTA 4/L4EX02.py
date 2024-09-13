"""
2. Elabore um algoritmo que leia dois números, some cinco ao de menor valor,
 compare os dois valores e mostre o maior.
"""

x= int(input("digite um numero"))
y= int(input("digite um numero"))
if(x<y):
    x= x+5
else:
    y= y+5
    if(x>y):
        print("o maior numero é",x)
    else:
        print("o maior numero é",y)
