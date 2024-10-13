"""
11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 

se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.

"""

nome=input("Digite seu nome:")

a=float(input("Digite a primeira nota:"))
b=float(input("Digite a segunda nota:"))
c=float(input("Digite a terceira nota:"))
d=float(input("Digite a quarta nota:"))

soma= a + b + c + d

media= soma / 4

if media > 7:
    print(f"{nome} sua media é:{media} você foi aprovado!")
else:
    print(f"{nome} sua media é:{media} você foi reprovado!")
