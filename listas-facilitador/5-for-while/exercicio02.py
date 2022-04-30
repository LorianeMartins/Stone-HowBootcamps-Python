"""Escreva um programa que exiba uma tabela de conversão de temperatura para graus Celsius e graus Fahrenheit. 
A tabela deve incluir linhas para todas as temperaturas entre 0 e 100 graus Celsius que são múltiplos de 10 graus Celsius. 
Dê um título apropriado para cada coluna. 
A fórmula para converter entre graus Celsius e graus Fahrenheit podem ser encontrados na Internet (faz parte do exercício pesquisar!)"""


print("°C | °F")

for temp_celsius in range (0, 100, 10):

    temp_fahrenheit = (temp_celsius * 9 / 5) + 32
    
    print(f"{temp_celsius:2.0f} | {temp_fahrenheit}")