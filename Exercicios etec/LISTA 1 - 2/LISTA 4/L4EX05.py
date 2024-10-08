"""
5. Elabore um algoritmo que leia três números some cinco ao menor valor e
mostre o resultado.
"""

x= int(input("digite o primeiro numero"))
y= int(input("digite o segundo numero"))
z= int(input("digite o terceiro numero"))
if(x<=y and x<=z):
    x= x+5
    print("o resultado é",x)
elif(y<=z):
    y= y+5
    print("o resultado é",y)
else:
    z= z+5
    print("o resultado é",z)
