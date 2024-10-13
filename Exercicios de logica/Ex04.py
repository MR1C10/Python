"""
4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.
"""
"""
# Jeito simples

a=int(input("Digite um número:"))
antecessor= a-1
sucessor= a+1
print(f"Antecessor: {antecessor}, Número: {a}, Sucessor: {sucessor}")
"""
# Jeito mais complexo e denecessario :)

# Função para verificar o antecessor e sucessor
def antecessor_sucessor(numero):
    antecessor= numero-1 
    sucessor= numero+1
    return antecessor, sucessor

x=int(input("Digite um número:"))

passando=antecessor_sucessor(x)# Passando o valor da entrada para a função

ante= passando[0]
suce= passando[1]
print(f"antecessor:{ante} sucessor{suce}")
