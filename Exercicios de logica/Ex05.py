"""
5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário,
calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado.
(Base para o Salário mínimo R$ 1.293,20).
"""

salario_minimo= 1293.20 # Valor do salario minimo 

valor_salario=float(input("Digite um numero")) # Valor do salario do usuario

quantidade_de_sarios= valor_salario/ salario_minimo # Calculo para descobir quantos salarios o usuaro ganha

print(f"Você ganha {quantidade_de_sarios:.2f} salarios minimos")