"""
2 - Faça um algoritmo para receber um número qualquer e imprimir na tela
se o número é par ou ímpar, positivo ou negativo.
"""

# Jeito simples

numero=int(input("Digite um número:"))

# Aqui vericamos se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é: Par")
else:
    print(f"O número {numero} é: Ímpar ")


# Aqui verificamos se o numero é negativo ou positivo
if numero < 0:
    print(f"O número {numero} é: Negativo")
elif numero > 0:
    print(f"O número {numero} é: Positivo")
# Zero é um numero par, mas não é positivo nem negativo
else: 
    print("O número é: Zero")

# Jeito mais complexo e denecessario :)
"""
# Função para verificar se o número é par ou impar, negativo ou positivo
def Verificar_numero(borabil):
    if borabil % 2==0:
        par_ou_inpar= "Par"
    else:
        par_ou_inpar= "Ímpar"
    
    if borabil<0:
        positivo_ou_negativo= "Negativo"
    else:
        positivo_ou_negativo= "Positivo"
    
    return par_ou_inpar, positivo_ou_negativo

numero=int(input("Digite um número:"))

# Passando o valor da entrada para a função
pasando= Verificar_numero(numero)

# Atribuindo o resultado as variaveis a e b
a= pasando[0]
b= pasando[1]

#Mostrando os resultados
print(f"O número é {a}")
print(f"O número é {b}")]
"""