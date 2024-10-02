"""
10. Crie um algoritmo que leia dois números, multiplique o menor por 10, e divida
o maior por 2, some os seus valores e verifique se o resultado e par, em caso
afirmativo exiba a mensagem, o resultado é par, caso contrario, exiba a
mensagem, o resultado é impar.
"""

x= int(input("Digite um número: "))
y= int(input("Digite um número: "))
if(x<y):
    x= x*10
    y= y/2
else:
    y= y*10
    x= x/2

z= x+y

if (z % 2 == 0):
    print(f"O número {z} é par.")
else:
    print(f"O número {z} é ímpar.")
    