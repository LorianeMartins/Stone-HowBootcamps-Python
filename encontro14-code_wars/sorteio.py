import csv
from collections import defaultdict
from random import choice


# 2 equipes completas ganham da stone
# 1 equipe completa ganha da how
# 3 ganham da stone individual

brindes = {"how": 5, "stone": 13}

equipes = defaultdict(list)

# Está na documentação como abrir arquivo csv
with open("encontro14-code_wars/sorteio.csv") as csvfile:
    arquivo = csv.reader(csvfile, delimiter = ";", quotechar = "|")
    for linha in arquivo:
        nome_aluno = linha[1].strip().replace("  ", " ")
        numero_equipe = int(linha[0])
        equipes[numero_equipe].append(nome_aluno)


# 1 - 40 -> 2 sorteios Stone
# 1 - 40 -> 1 sorteios How
# 3 pessoas -> 3 brindes individuais da Stone

for _ in range(2): 

    print("\nSorteio do brinde da Stone!")

    equipe_sorteada = choice(list(equipes.keys()))
    pessoas_sorteadas = equipes[equipe_sorteada]

    print(f"\nA equipe sorteada foi {equipe_sorteada}...")

    for pessoa in pessoas_sorteadas:
        print(f"Parabéns {pessoa}, você ganhou um brinde da Stone!")

    equipes.pop(equipe_sorteada)
    print("*" * 60)




print("\nSorteio do brinde da How!")

equipe_sorteada = choice(list(equipes.keys()))
pessoas_sorteadas = equipes[equipe_sorteada]

print(f"\nA equipe sorteada foi {equipe_sorteada}...")

for pessoa in pessoas_sorteadas:
        print(f"Parabéns {pessoa}, você ganhou um brinde da Stone!")

equipes.pop(equipe_sorteada)
print("*" * 60)



pessoas_nao_sorteadas = []

for nomes in equipes.values():
    pessoas_nao_sorteadas.extend(nomes)



print("\nSorteio individual do brinde da Stone! \o/\n")
for _ in range(3):

    pessoa_sortuda = choice(pessoas_nao_sorteadas)

    pessoa_sortuda_indice = pessoas_nao_sorteadas.index(pessoa_sortuda)

    print(f"Parabéns {pessoa_sortuda}! Você ganhou um brinde individual!")

    pessoas_nao_sorteadas.pop(pessoa_sortuda_indice)