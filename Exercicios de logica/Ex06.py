"""
6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.
"""

x=int(input("Digitye um numero:"))

aumento=5 # Reajuste de 5% 

amostradinho= x + (x * aumento/100) # calculo para realizar o reajuste
print(f"{x} + 5% = {amostradinho}")