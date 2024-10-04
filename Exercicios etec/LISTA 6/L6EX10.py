"""
10. Elabore um algoritmo que leia um número entre cinco e dez e mostre o seu
valor na tela. 
"""

x=int(input("Digite um numero entre 5 e 10:"))
while(x<=5 or x>=10):
    print("Numero invalido! Digite um numero entre 5 e 10:")
    x=int(input("Digite um numero entre 5 e 10:"))
    if x<=5 or x<=10:
        print(x)