"""
12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, 
conforme a escolha da forma de pagamento pelo comprador e imprima na tela o valor final do produto a ser pago. 
Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

Tabela de Código de Condições de Pagamento

 

 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

 2 - À Vista no cartão de crédito, recebe 10% de desconto

 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
"""

def forma_de_pagamento(x):
    
    paga = {   
        1: "dinheiro",
        2: "pix",
        3: "cartao_a_vista",
        4: "cartao_parcelado_ate_2x",
        5: "carta_parcelado_2x_ou_mais"
    }
    return paga.get(x,"Numero invalido")

valor=float(input("Qual o valor do protuduto?:"))
pagamento=int(input("Qual a forma de pagamento?\n1: dinheiro\n2: pix\n3: cartao a vista\n4: cartao parcelado em ate 2x\n5: catao parcelado em 3x ou mais\nDigite a forma de pagameto:"))

forma=forma_de_pagamento(pagamento)

print(forma)

if forma == "pix" or forma == "dinheiro":
    desconto=15
    a= valor - (desconto / 100) * valor
    print(f"Valor com 15% de desconto {a}")

elif forma == "cartao_a_vista":
    desconto=10
    a= valor - (desconto / 100) * valor
    print(f"Valor com 10% de desconto {a}")

elif forma == "cartao_parcelado_ate_2x":
    print(f"Valor para pagamento{valor}")

else:
    forma == "carta_parcelado_2x_ou_mais"
    acrecimo=10
    a= valor + (acrecimo / 100) * valor
    print(f"Valor com 10% de acrecimo {a}")
                