"""
7. Elabore um algoritmo que leia dois números, um maior que dez e outro menor
que 5, mostre os números lidos. 
"""

x=int(input("Digite um numero maior que 10:"))
y=int(input("Digite um numero menor que 5:"))

while(x<0):
    print("Numero invalido! Digite um numero maior que 10:")
    x=int(input("Digite um numero:"))

while(y>5):
    print("Numero invalido! Digite um numero menor que 5:")
    y=int(input("Digite um numero menor que 5:"))

print(f"Numero maior que 10: {x}")
print(f"Numero menor que 5: {y}")

"""
x=int(input("Digite um numero maior que 10:"))
while(x<0):
    print("Numero invalido! Digite um numero maior que 10:")
    x=int(input("Digite um numero:"))

y=int(input("Digite um numero menor que 5:"))
while(y>5):
    print("Numero invalido! Digite um numero menor que 5:")
    y=int(input("Digite um numero menor que 5:"))

print(f"Numero maior que 10: {x}")
print(f"Numero menor que 5:{y}")
"""

"""
x=int(input("Digite um numero:"))
y=int(input("Digite um numero:"))

while(x<10):
    print(x)
    x=int(input("Digite um numero:"))

while(y>5):
    print(y)
    y=int(input("Digite um numero:"))
    
if x >10 and y<5:
    print(x)
    print(y)
""" 