"""
9. Crie um algoritmo que leia um número maior que 20 e mostre na tela os
números entre o número digitado e o número 1 em ordem decrescente. 
"""

x=int(input("Digite um numero maior que 20:"))

while (x<=20): # Verifica se o numero digitado é maior que 20
    print("Numero invalido! Digite um numero maior que 20:")
    x=int(input("Digite um numero maior que 20:"))

while(x>1): # Enquanto x for maior que 1 lhe é retirado 1, assim mostrando os numeros em ordem decrecente 
    x=x-1
    print(x)