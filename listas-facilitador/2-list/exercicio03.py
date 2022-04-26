"""Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições."""

lista = [1, 2, 3, 4, 5, 6]

maior = max(lista)
menor = min(lista)

indice_maior = lista.index(maior)
indice_menor = lista.index(menor)

print(f"\nO maior valor da lista é {maior} e está na posição {indice_maior}.")
print(f"O menor valor da lista é {menor} e está na posição {indice_menor}.")