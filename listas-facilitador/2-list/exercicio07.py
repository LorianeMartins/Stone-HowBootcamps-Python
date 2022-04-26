"""Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.
Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para string."""

lista_strings = ["1", "7", "99", "15"]

lista_numeros = []

for string in lista_strings: 

    numero = int(string)
    lista_numeros.append(numero)

print(f"A lista de inteiros é {lista_numeros}")

lista_conversao_num_string = list(map(str, lista_numeros))

print(f"A lista de inteiros convertida para lista de strings novamente é {lista_conversao_num_string}")