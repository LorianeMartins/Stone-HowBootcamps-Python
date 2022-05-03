from collections import defaultdict
from random import randint, seed

LETRAS = ("B", "I", "N", "G", "O")


def min_max(letra: str) -> tuple[int]:
    """Gera o valor mínimo e máximo para letra dada.
    
    Args:
        letra(str): letra input
    
    Returns:
        tuple[int]: valores mínimo e máximo 
    """

    # Coloca só os intervalos, não todas as possibilidades de cada intervalo
    intervalo = { "B": (1, 15), "I": (16, 30), "N": (31, 45), "G": (46, 60), "O": (61, 75)}

    # Coletar o número mínimo e máximo de cada letra
    minimo, maximo = intervalo[letra][0], intervalo[letra][1]

    return minimo, maximo

# Passo 0:
def gerar() -> defaultdict[str, list[int]]:
    """Gera uma cartela com 5 números para cada letra."""
 
    cartela = defaultdict(list)

    for letra in LETRAS: 

        minimo, maximo = min_max(letra)
       
        while len(cartela[letra]) < 5: 

            # Gerar um número aleatório inteiro
            num_aleatorio = randint(minimo, maximo)

            # Verificar se o número já foi gerado para aquela letra
            if num_aleatorio in cartela[letra]:
                continue
        
            # Colocar número aleatório na lista
            cartela[letra].append(num_aleatorio)

            # Ordena os números 
            cartela[letra].sort()

    return cartela

# Passo 1:
def imprime(cartela: dict[str, list[int]]) -> None:
    """Formata a cartela para imprimir na tela
    
    Args:
        cartela (dict[str, list[int]]): cartela de entrada
    """
    print(" B  I  N  G  O")

    for linha in range(5):

        # Coleta o primeiro elemento de cada lista que está dentro de cartela e devolve uma lista com tais      elementos
        # Converte cada elemento da lista de inteiros para string e devolver na forma de lista de string
        # Método de string que coloca mais um dígito: .zfill()

        lista_str = [str(lista[linha]).zfill(2) for lista in cartela.values()]

        # Devolve os números somente como string separados por um conector, um espaço
        string = " ".join(lista_str)

        # Imprime os valores da cartela já formatada 
        print(string)

def marca_numero(cartela: defaultdict, letra: str, numero: int, caracter: str):

    # Coletar o índice da lista do número sorteado 
    indice_num_sorteado = cartela[letra].index(numero)

    cartela[letra][indice_num_sorteado] = caracter
    
    return cartela

def verifica_numero_sorteado(cartela: defaultdict, letra: str, numero: int):

    if numero in cartela[letra]:
        print("Você acertou um número!")
        return True
    print("Você errou um número!")
    return False

# Passo 3: 
def verifica_cartela(cartela: defaultdict):

    for linha in range(5): 

        lista_numeros = [lista[linha] for lista in cartela.values()]

        if lista_numeros.count("**") == len(lista_numeros):
            print(f"A linha {linha + 1} da cartela foi totalmente preenchida! BINGO!")
        

    for letra in cartela: 

        if cartela[letra].count("**") == len(cartela[letra]):
            print(f"\nA coluna {letra} da cartela foi totalmente preenchida! BINGO!")
        
            
    

        


