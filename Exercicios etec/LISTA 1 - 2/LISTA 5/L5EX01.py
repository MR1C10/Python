"""
1. Elabore um algoritmo que receba um número e escreva na tela o dia da semana
corresponde, considerando que o domingo é o primeiro dia da semana e
corresponde ao numero um.
"""

x= int(input("digite um número de 1 a 7:"))

if(x==1):
    print("Domingo")
elif x==2:
    print("Segunda-feira")
elif x==3:
    print("Terça-feira")
elif x==4:
    print("Quarta-feira")
elif x==5:
    print("Quinta-feira")
elif x==6:
    print("Sexta-feira")
elif x==7:
    print("Sábado")
else:
    print("Número invalido")