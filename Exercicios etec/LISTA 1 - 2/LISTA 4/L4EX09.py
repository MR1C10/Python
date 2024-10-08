"""
9. Desenvolva um algoritmo que leia quatro números, some os dois primeiros e
subtraia os dois últimos, some os resultados e mostre a seguinte mensagem,
resultado maior que dez, caso a afirmação esteja correta ou resultado menor
ou igual a dez.
"""

x= int(input("digite um numero"))
y= int(input("digite um numero"))
z= int(input("digite um numero"))
w= int(input("digite um numero"))
a= x+y
b= z-w
c= a+b
if(c>10):
    print("Resultado maior que dez",c)
else:
    print("Resultado menor ou igual a dez",c)