"""
3. Crie um algoritmo que leia dois números e mostre os números entre eles.
"""

x=int(input("Digite o primeiro numero"))
y=int(input("Digite outro numero"))
for z in range(x+1,y):
    print (z)
for z in range(y+1,x):
    print(z)