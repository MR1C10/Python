"""
8 - Faça um algoritmo que leia três valores inteiros diferentes 
e imprima na tela os valores em ordem decrescente.
"""

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

def iguais():
    global a, b, c
    
    while a == b or a == c:
        print("Os numeros devem ser diferentes")
        a = int(input("Redigite o primeiro numero: "))
    
    while b == a or b == c:
        print("Os numeros devem ser diferentes")
        b = int(input("Redigite o segundo numero: "))

def decrecente(a,b,c):

    numeros= sorted([a,b,c], reverse=True)     
    
    return numeros

iguais()
ordem=decrecente(a,b,c)
print(ordem)