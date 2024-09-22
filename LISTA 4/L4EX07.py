"""
7. Crie um algoritmo que leia três números e mostre seus valores em ordem
crescente.
"""

x= int(input("digite um numero"))
y= int(input("digite um numero"))
z= int(input("digite um numero"))
if x <= y and x <= z:
    if y <= z:
        print(x, y, z)
    else:
        print(x, z, y)
elif y <= x and y <= z:
    if x <= z:
        print(y, x, z)
    else:
        print(y, z, x)
else:
    if x <= y:
        print(z, x, y)
    else:
        print(z, y, x)
        