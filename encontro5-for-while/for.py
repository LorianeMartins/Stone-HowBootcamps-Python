"""Estrutura de repeteição - for"""

# Dicionário vazio com nome como chave e uma lista como valor
fechamento = dict()

numero_alunos = int(input("Querido usuário, quantos alunos são? "))

numero_notas = int(input("Quantas notas por aluno? "))

for _ in range(numero_alunos):

    nome = input("Qual o nome do aluno? ")

    fechamento[nome] = []

    for _ in range(numero_notas):

        nota = int(input(f"Digite a nota do {nome}: "))

        fechamento[nome].append(nota)

for aluno, notas in fechamento.items():

    media = sum(notas) / len(notas)

    print(f"A média do aluno {aluno} foi {media}")