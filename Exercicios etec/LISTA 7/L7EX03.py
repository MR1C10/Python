"""
3. Criar um algoritmo que leia quatro notas de cinco alunos e calcule e mostre as
médias e as notas dos alunos.
"""

notas=[]

notas.append(float(input("Digite a nota de matematica:")))
notas.append(float(input("Digite a nota de portugues:")))
notas.append(float(input("Digite a nota de ciencias:")))
notas.append(float(input("Digite a nota de geografia:")))

x= len(notas)
print(f"Temos {x} notas cadastradas")

for i in notas:
    print(i)

# Duas formas de adicionar as notas na lista
"""
notas = []

notas.append(int(input("Digite a nota de matemática:")))
notas.append(int(input("Digite a nota de português:")))

print(notas)
"""
"""
notas = [0] * 4  # Inicializa uma lista com 4 elementos

notas[0] = int(input("Digite a nota de matemática:"))
notas[1] = int(input("Digite a nota de português:"))

print(notas)
"""