"""Módulos"""

# Definindo uma função para cálculo de média 
# A função recebe a lista como parâmetro e retorna um float

def calcula_media(valores: list) -> float: 
    """Calcula a média aritimética"""

    # Retorna o cálculo da média 
    return sum(valores) / len(valores)

# Função para cálculo de média ponderada
# A função recebe `valores` que é uma lista, `pesos` que é uma tupla e retorna um float 
# O parâmetro pesos é opcional. Se não for passado: 
    # Cria-se uma tupla com vários números do mesmo tamanho(número de elementos) do paramâmetro `valores`


def calcula_media_ponderada(valores: list, pesos: tuple or None = None) -> float: 

    if not pesos: 

        # Cria-se uma tupla cheia de 1, com mesmo número de elementos de `valores`
        pesos = (1, ) * len(valores)

    numerador = 0

    denominador = sum(pesos)

    # Iterando por cada par de valor, peso
    for valor, peso in zip(valores, pesos): 

        numerador += valor * peso

    return numerador / denominador