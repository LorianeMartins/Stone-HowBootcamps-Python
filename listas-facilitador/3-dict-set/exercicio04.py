"""Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário"""

entrada = {1: "vermelho", 2: "azul", 3: "marrom"}

lista = list(entrada.items())

for indice in range(len(lista)): 
    print(f"A string '{lista[indice][1]}' possui tamanho {len(lista[indice][1])}")
    
    
#Outra forma de fazer: mais clean
saida = dict()

for chave, valor in entrada.items(): 
    saida[chave] = len(valor)

print(saida)