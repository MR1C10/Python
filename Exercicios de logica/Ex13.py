"""
13 - Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 
"""

nome=input("Digite seu nome:")
idade=int(input("Digite sua idade:"))
peso=float(input("Digite seu peso:"))

if idade >= 18:
    print(f"Seu nome é: {nome} \nSeu peso é: {peso} \nVocê é maior de idade")
else:
    idade < 18
    print(f"Seu nome é: {nome} \nSeu peso é: {peso} \nVocê é menor de idade")