"""
8. Desenvolva um algoritmo que leia um número menor que cinco e mostre os
números pares entre o número lido e o número 20.
"""

x=int(input("digite um numero menor que 5:"))
while(x>=5):
    print("Numero invalido! Digite um numero menor que 5:")
    x=int(input("digite um numero menor que 5:"))

for a in range(x,21):
    if a % 2 == 0:
        print(a)