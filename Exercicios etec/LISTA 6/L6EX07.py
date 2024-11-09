"""
7. Elabore um algoritmo que leia dois números, um maior que dez e outro menor
que 5, mostre os números lidos. 
"""

n = 0

while (n < 2):
    w = int(input("Digite um número:")) 
    if w < 5:
        print(w)
        n = 1 
        
        y = 5
        while (y < 11):
            y=int(input("Digite um número:"))
        print(y)
        n = 2

    elif w > 10:
        print(w)
        n = 1
        
        x = 10
        while (x > 4):
            x=int(input("Digite um número:"))
        print(x)
        n = 2


"""
x=int(input("Digite um numero:"))

while not (x < 5 or x > 10):
    x=int(input("Numero invalido! Digite um numero["))

y=int(input("Digite um numero:"))
while (x < 5 and y > 10) or (x > 10 and y < 5):
    y=int(input("Numero invalido! Digite outro numero:"))

print(f"{x}\n{y}")
"""

# Forma 1
"""
x=int(input("Digite um numero maior que 10:"))
y=int(input("Digite um numero menor que 5:"))

while(x<10):
    print("Numero invalido! Digite um numero maior que 10:")
    x=int(input("Digite um numero:"))

while(y>5):
    print("Numero invalido! Digite um numero menor que 5:")
    y=int(input("Digite um numero menor que 5:"))

print(f"Numero maior que 10: {x}")
print(f"Numero menor que 5: {y}")
"""

# Forma 2
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


# Forma 3
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