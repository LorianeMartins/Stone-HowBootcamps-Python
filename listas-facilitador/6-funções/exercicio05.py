"""Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor (lista) de 1 a 9 parece ser mais simples que usar uma matriz 3x3."""

from itertools import permutations

todos_os_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Repetição para gerar todas as combinações possíveis de quadrados. 

# 9 possibilidades para primeira posição, 8 para segunda posição, 7 para terceira, e assim por diante...
# 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 362.880
# Para cada uma das possibilidades, verificamos se a soma das colunas, linhas e diagonais resultam em um mesmo número

for combinacao in permutations(todos_os_numeros, 9):

    # Equivalente à combinacao[0] + combinacao[1] + combinacao[2]
    soma_primeira_linha = sum(combinacao[:3])

    soma_segunda_linha = sum(combinacao[3:6])

    soma_terceira_linha = sum(combinacao[6:])

    soma_primeira_coluna = sum(combinacao[::3])

    soma_segunda_coluna = sum(combinacao[1::3])

    soma_terceira_coluna = sum(combinacao[2::3])

    soma_primeira_diagonal = combinacao[0] + combinacao[4] + combinacao[8]
    soma_segunda_diagonal = combinacao[2] + combinacao[4] + combinacao[6]

    somas = (
        soma_primeira_linha,
        soma_segunda_linha,
        soma_terceira_linha,
        soma_primeira_coluna,
        soma_segunda_coluna,
        soma_terceira_coluna,
        soma_primeira_diagonal,
        soma_segunda_diagonal
    )

    if(len(set(somas)) == 1):
        print("Temos um quadrado mágico!")

        print(
            f" {combinacao[0]} {combinacao[1]} {combinacao[2]}\n {combinacao[3]} {combinacao[4]} {combinacao[5]}\n {combinacao[6]} {combinacao[7]} {combinacao[8]}"
        )
