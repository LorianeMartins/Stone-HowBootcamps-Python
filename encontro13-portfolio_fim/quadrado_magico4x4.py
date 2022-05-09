"""
Enunciado:
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, 
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado de lado 4, com números de 1 a 16:
01  05  09  16
06  07  02  10
08  03  04  11
12  15  14  13
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar uma lista de 1 a 16 parece ser mais simples que usar uma matriz 4x4.
Extra: Permita que o usuário indique o tamanho do cubo (2x2, 3x3, 4x4, etc.)
"""

from itertools import permutations

tamanho = int(input("Digite o tamanho do cubo: "))

qtd_numeros = tamanho * tamanho

lista_numeros = []

for _ in range(tamanho):

    numeros = []
    
    for numero_cubo in range(tamanho):
        
        numeros.append(numero_cubo+1)      
        
    lista_numeros.append(numeros)

print(lista_numeros)

    
    
   




 

    