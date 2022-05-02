"""Importaçao do módulo"""

from calculo import calcula_media_ponderada

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