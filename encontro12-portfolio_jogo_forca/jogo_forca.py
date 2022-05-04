"""
Construa um jogo da forca!

A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.
Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

# Meus módulos
from utils import WORDS, STATUS
from funcoes_jogo import * 

secret_word = get_secret_word(WORDS)
correct_letters = []  # variável que armazena as letras corretas já jogadas
wrong_letters = []  # variável que armazena as letras incorretas já jogadas
error = 0  # erro inicial
attempts = 6  # tentativas

while game_continue(correct_letters, secret_word, attempts, error, STATUS):
    print_game_board(secret_word, correct_letters, wrong_letters, error, attempts, STATUS)
    letter = read_input_player()
    result = guess_letter(letter, secret_word, correct_letters, wrong_letters)
    if not result:
        error += 1

   

