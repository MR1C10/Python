"""
8. Elabore um algoritmo que leia um número, se ele for maior que dez, some
cinco ao seu valor, se for menor ou igual, some 20 e mostre se o resultado for
maior que vinte e cinco.
"""

x= int(input("digite um numero"))
if(x>10):
    x= x+5
else:
    x= x+20
if(x>25):
    print(x)
