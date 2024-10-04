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


# Outra alternativa
""" 
x= int(input("Digite um número de 1 a 7:"))

def dia_da_semana(x):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }
    return dias.get(x,"Numero invalido")

resultado = dia_da_semana(x)

print(resultado)
"""
