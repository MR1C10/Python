"""
2. Desenvolva um algoritmo que leia cinco números e armazene um vetor, após
receber os números ordene os dados em ordem crescente e mostre os valores. 
"""
    
valor1=int(input("Digite um número:"))
valor2=int(input("Digite um número:"))
valor3=int(input("Digite um número:"))
valor4=int(input("Digite um número:"))
valor5=int(input("Digite um número:"))

armazenar= [valor1, valor2, valor3, valor4, valor5]

def ordenar(x):
    
    ordem= sorted(x)
    
    return ordem

ordenados= ordenar(armazenar)

print(ordenados)


# Entendendo como armazenar os valores no vetor
"""
valor1=int(input("Digite um número:"))
valor2=int(input("Digite um número:"))
valor3=int(input("Digite um número:"))
valor4=int(input("Digite um número:"))
valor5=int(input("Digite um número:"))

armazenar= [valor1, valor2, valor3, valor4, valor5]

print(armazenar)
"""