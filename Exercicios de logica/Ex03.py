"""
3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais,
deverá somar os dois valores, caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos
deve-se atribuir o resultado a uma variável C e imprimir seu valor na tela.
"""

a=int(input("Digite um numero:"))
b=int(input("Digite um numero:"))

if a == b:
    c=a+b
    print(c)
else:
    c=a*b
    print(c)