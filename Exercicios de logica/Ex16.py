"""
16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é 

equilátero, isósceles ou escaleno.
"""

lado1=int(input("Digite o valor do primeiro lado do triângulo:"))   
lado2=int(input("Digite o valor do segundo lado do triângulo:"))
lado3=int(input("Digite o valor do terceiro lado do triângulo:"))

def triangulo(a, b, c):
    
    if lado1 == lado2 == lado3:
        return "O triângulo é equilatero"

    elif (lado1 == lado2 != lado3) or (lado1 == lado3 != lado2) or (lado2 == lado3 != lado1):
        return "O triangulo é isósceles"
    
    else:
        lado1 != lado2 != lado3
        return "O triangulo é escaleno"

medida= triangulo(lado1, lado2, lado3)

print(medida)