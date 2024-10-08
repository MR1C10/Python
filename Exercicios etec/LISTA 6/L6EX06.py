"""
6. Crie um algoritmo que leia um número menor que 10 e mostre o seu valor. 
""" 

x=int(input("Digite um numero:"))
while(x>10):
    print("o numero digitado é maior que 10!")
    x=int(input("Digite um numero:"))  
print(x)

# Outra alternativa
"""
x=int(input("Digite um numero:"))

if x<10:
    print(x)
else:
    print("o numero digitado é maior que 10")
    while(x>10):
        x=int(input("DIgite um numero:"))  
"""