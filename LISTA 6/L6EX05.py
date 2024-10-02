"""
5. Desenvolva um algoritmo que leia três números e mostre na tela os números
entre os dois maiores. 
"""
#Codigo feio, arrumar assim que possivel
x=int(input("Digite um numero:"))
y=int(input("Digite outro numero:"))
z=int(input("Digite mais um numero:"))

if x>y and x>z:# x e y maior 
    if y>z:
        for a in range(y+1,x):
            print(f"numeros entre {y} e {x} são:", a)

if x>y and x>z:# x e z maior
    if z>y:
        for a in range(z+1,x):
            print(f"numeros entre {z} e {x} são:", a)

if y>x and y>z:# y e x maior 
    if x>z:
        for a in range(x+1,y):
            print(f"numeros entre {x} e {y} são:", a)

if y>x and y>z:# y e z maior
    if z>x:
        for a in range(z+1,y):
            print(f"numeros entre {z} e {y} são:", a)

if z>x and z>y:# z e x maior
    if x>y:
        for a in range(x+1,z):
            print(f"numeros entre {x} e {z} são:", a)
 
if z>x and z>y:# z e y maior
    if y>x:
        for a in range(y+1,z):
            print(f"numeros entre {y} e {z} são:", a)
else:
    print("Não a numeros entre as variaveis")
