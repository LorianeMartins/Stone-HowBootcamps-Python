"""Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. 
Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. 
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. 
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo.
Obs: tabela no enunciado do exercício"""

nivel_sonoro = float(input("Informe o valor de nível sonoro em decibéis: "))

if nivel_sonoro > 130:
    print(f"Nível sonoro acima do valor máximo permitido.")
elif nivel_sonoro == 130: 
    print(f"Nível sonoro de uma britadeira.")
elif 106 < nivel_sonoro < 130: 
    print(f"Nível sonoro entre cortador de grama e britadeira.")
elif nivel_sonoro == 106:
    print(f"Nível sonoro de um cortador de grama.")
elif 70 < nivel_sonoro < 106: 
    print(f"Nível sonoro entre despertador e cortador de grama.")
elif nivel_sonoro == 70:
    print(f"Nível sonoro de um despertador.")
elif 40 < nivel_sonoro < 70: 
    print(f"Nível sonoro entre cômodo em silêncio e despertador.")
elif nivel_sonoro == 40:
    print(f"Nível sonoro de cômodo em silêncio.")
else:
    print("Nível sonoro abaixo do mínimo.")