from random import choice

def get_secret_word(words: list) -> str:
    """Devolve uma palavra aleatória de uma lista.
    
    Args: 
        words(list): lista possíveis palavras

    Returns: 
        str: palavra secreta escolhida aleatóriamente
    """

    return choice(words).lower()

def print_game_board(palavra: str, correct_letters: list, wrong_letters: list, error: int, attempts: int, status: tuple[str]) -> None:
    """Imprime a situação atual do jogo.
    
    Args: 
        letra(str): letra de entrada
        palavra(str): palavra secreta escolhida aleatoriamente
        correct_letters(list): lista de letras corretas da palavra secreta
        wrong_letters(list): lista de letras erradas da palavra secreta 
        error(int): número de tentativas erradas do usuário
        attempst(int): número de tentativas do usuário
        status(list[str]): impressão do status do usuário no jogo
    
    Returns: 
        None
    """
    encoded_word = ""

    for letra in palavra:
        if letra not in correct_letters:
            # encoded_word = encoded_word + "_"
            encoded_word += "_"
        
        else:
            encoded_word += letra

    if error <= attempts:
        print(status[error])

        print(encoded_word)
    
    print(f"\nLetras corretas: {' '.join(correct_letters)}")
    
    print(f"\nLetras erradas: {' '.join(wrong_letters)}")

    return None

def read_input_player() -> str:
    """Lê uma letra do usuário.
    
    Returns:
        str: letra digitada pelo usuário para comparar com a palavra secreta
    """
    letra = input("Digite uma letra: ").lower()

    while len(letra) != 1 or not letra.isalpha():
        print("Digite apenas um caracter: ")
        letra = input("Digite uma letra: ").lower()
    
    return letra

def guess_letter(letra: str, palavra: str, correct_letters: list, wrong_letters: list) -> bool:
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada.
    
    Args: 
        letra(str): letra jogada pelo usuário
        palavra(str): palavra secreta escolhida aleatóriamente na lista de palavras
        correct_letters(list): lista com as letras corretas da palavra
        wrong_letters(list): lista com as letras erradas da palavra

    Returns:
        bool: True or False
    
    """

    if letra in palavra and letra not in correct_letters:
        correct_letters.append(letra)
        return True

    elif letra not in palavra and letra not in wrong_letters:
        wrong_letters.append(letra)
        return False
                
    else:
        print("Essa letra já foi jogada!")
        return False

def game_continue(correct_letters: list, secret_word: str, attempts: int, error: int, status: tuple[str]) -> bool:
    """Função que decide se jogo já encerrou ou não.
    
    Args: 
        correct_letters(list): lista de letras corretas da palavra secreta 
        secret_word(list): palavra secreta escolhida aleatoriamente 
        attempts(int): tentativas disponíveis
        error(int): número de erros cometidos 
        status(list[str]): printa o status do jogo 
    
    Return:
        true or false
    """

    if set(correct_letters) == set(secret_word):
        print("Você venceu o jogo!")
        return False

    elif attempts <= error: 
        print(status[error])
        print(f"A palavra secreta é {secret_word}")
        return False

    return True
