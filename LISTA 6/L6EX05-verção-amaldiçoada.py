"""
5. Desenvolva um algoritmo que leia três números e mostre na tela os números
entre os dois maiores. 
"""

x=int(input("Digite um numero:"))
y=int(input("Digite outro numero:"))
z=int(input("Digite mais um numero:"))

m1=m1=None

if x>y and x>z:
    m1=x
    m2=y if y>z else z
    for a in range(m2+1,m1):
        print(f"numeros entre {m2} e {m1} são:", a)
elif y>x and y>z:
    m1=y
    m2=x if x>z else z
    for a in range(m2+1,m1):
        print(f"numeros entre {m2} e {m1} são:", a)
else:
    m1=z
    m2=x if x>y else y
    for a in range(m2+1,m1):
        print(f"numeros entre {m2} e {m1} são:", a)
if m1<m2-1:
    for a in range(m2+1,m1):
        print(f"numeros entre {m2} e {m1} são:", a)
else:
    print("Não a numeros entre as variaveis")