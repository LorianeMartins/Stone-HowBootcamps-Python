"""Escreva um programa que leia três números e que imprima o maior e o menor."""

lista = []

for _ in range(3): 
    
    numero = int(input("Informe um número inteiro: "))
    lista.append(numero)

maior = max(lista)
menor = min(lista)

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
    