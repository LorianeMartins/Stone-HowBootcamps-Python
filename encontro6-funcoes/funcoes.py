"""Funções"""

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

# Criação de um dicionário vazio, que vai receber o nome do aluno como chave e uma lista de notas como valor
fechamento = dict()

# Recebe do usuário quantos alunos serão:
numero_alunos = int(input("Digite o número de alunos: "))

numero_notas = int(input("Digite o número de notas: "))

for _ in range(numero_alunos):

    nome = input("Digite o nome do aluno: ")

    # Cria no dicionário uma chave com o nome do aluno e o valor sendo uma lista vazia 
    fechamento[nome] = []

    for nota in range(numero_notas):

        nota = int(input(f"Digite a nota {nota+1} do {nome}: "))
        fechamento[nome].append(nota)

# Laço no dicionário para calcular a média de cada aluno e imprimir na tela
for aluno, notas in fechamento.items():

    # Chamamos a função 
    media_ponderada = calcula_media_ponderada(notas)

    # Imprime o nome do aluno e a média na tela 
    print(f"A média do aluno {aluno} foi {media_ponderada}")