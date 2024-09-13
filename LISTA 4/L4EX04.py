"""
4. Elabore um algoritmo que leia três números e mostre o maior
"""

x= int(input("digite o primeiro numero"))
y= int(input("digite o segundo numero"))
z= int(input("digite o terceiro numero"))
if(x>=y and x>=z):
    print("o maior numero é",x)
elif(y>=z):
    print("o maior numero é",y)
else:
    print("o maior numero é",z)
