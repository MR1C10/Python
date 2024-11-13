"""
15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, 
meses e dias essa pessoa ja viveu. Leve em consideração o ano com 365 dias e o mês com 30 dias.
(Ex: 5 anos, 2 meses e 15 dias de vida)
"""

mes_atual= 11 # Mude o valor para o mes corespondente 
ano_atual= 2024 # Mude o valor para o ano corespondente 
dia_atual= 7 # Mude o valor para o dia corespondente 

nascimento=int(input("Digite o ano em que vc nasceu:"))
dia=int(input("Digite o dia que vc nasceu:"))
mes=int(input("Digite o mês que vc nasceu:"))

anos= ano_atual - nascimento # quantos anos tem a pessoa

meses= mes_atual - mes # não mexe aqui que já deu bom!

if dia < dia_atual:
    dias=  (30 + dia_atual) - dia
else:
    dias= (30 - dia_atual) + dia

print(f"Você tem {anos} anos, {meses} meses e {dias} dias de vida")
