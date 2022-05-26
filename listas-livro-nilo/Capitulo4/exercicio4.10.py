"""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para
indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
+---------------------------------------+
| Preço por tipo e faixa de consumo    |
+---------------------------------------+
| Tipo        | Faixa (kWh)  | Preço   |
+=======================================+
| Residencial | Até 500      | R$ 0,40 |
|             | Acima de 500 | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000     | R$ 0,55 |
|             | Acima de 1000| R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000     | R$ 0,55 |
|             | Acima de 5000| R$ 0,60 |
+---------------------------------------+
"""
qtd_kwh = float(input("Informe a quantidade consumidade de kWh: "))
instalacao = input("Informe o tipo de instalação, R para residência, I para indústria ou C para comércio: ").upper()

if instalacao == "R":
    
    if qtd_kwh < 500: 
        preco = qtd_kwh * 0.40
    else: 
        preco = qtd_kwh * 0.65

elif instalacao == "I":
    
    if qtd_kwh < 1000: 
        preco = qtd_kwh * 0.55
    else: 
        preco = qtd_kwh * 0.60

elif instalacao == "C":
    
    if qtd_kwh < 5000: 
        preco = qtd_kwh * 0.55
    else: 
        preco = qtd_kwh * 0.60

else:

    print("Instalação inválida!")
    preco = 0 

print(f"O valor a ser pago é R${preco}")