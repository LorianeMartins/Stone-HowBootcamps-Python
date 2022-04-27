"""Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. 
Exemplos: 
•	Dada a entrada ABT-1234 o programa deveria exibir True
•	Dada a entrada JKL9999 o programa deveria exibir False
•	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False """

placa = input("Informe a placa do veículo: ")

if len(placa) != 8:

    resultado = False

else:
    if (placa.isupper() 
    
        and placa[:3].isalpha() 
        
        and placa[4:].isdigit() 
        
        and placa[3] == "-"):

            resultado = True
         
    else:
        
        resultado = False

print(f"\nA placa é válida? {resultado}")