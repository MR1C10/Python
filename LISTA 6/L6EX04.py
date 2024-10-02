"""
4. Elabore um algoritmo que leia um número e mostre a tabuado do número lido,
utilizando uma estrutura de repetição. 
"""

x=int(input("Digite um numero"))
for y in range(1, 11):
    z= x*y
    print(f"{x}x{y}=",z)

#Opção para definir quantas vezes será multiplicado
"""
x=int(input("Digite um numero"))
y=int(input("Digite um numero"))
for y in range(1, y+1):
    z= x*y
    print(f"{x}x{y}=",z)
"""

# y começa em 1 e vai até 10.
# A cada iteração, ele calcula a multiplicação e imprime o resultado.
# Após imprimir, y é incrementado em 1.
# Quando y atinge 11, o loop para.
"""
x=int(input("Digite um numero"))
y=1
while(y<=10):
    z=x*y
    print(f"{x}x{y}=",z)
    y+=1
"""
