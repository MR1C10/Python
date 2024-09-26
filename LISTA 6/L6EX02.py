"""
2. Desenvolva um algoritmo que leia um número e mostre na tela os números
entre o número lido e 20.
"""
x=int(input("Digite um numero"))

y=x
for x in range(x, 21):
    print (f"os numeros entre {y} e 20 são", x)

for x in range(21, x):
    print(f"os numeros entre 20 e {x} são", x)

#Outra alternativa
"""
while(x<20-1):
    x+=1
    print (x)

while(20<x-1):
    x-=1
    print(x)
"""
