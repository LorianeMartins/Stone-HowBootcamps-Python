""" Estrutura de repetição while """

fechamento = dict()

nome = input("Digite o nome do aluno: ")

fechamento[nome] = []

# Inicializa a condição que entrará no while
condicao = "S"

while condicao == "S":

    nota = int(input("Informe uma nota: "))

    fechamento[nome].append(nota)

    condicao = input("Deseja entrar com mais uma nota? S ou N?").upper()

    # Verificação
    if len(condicao) == 1 and condicao == "S":

        # Volta para o início do while
        continue

    elif len(condicao) == 1 and condicao == "N":

        # Interrompe o laço 
        break

    else: 
        print("Condição inválida! Digite uma condição válida!")

        condicao = input("Digite entrar com mais uma nota? S ou N? ")

for aluno, notas in fechamento.items():

    media = sum(notas) / len(notas)

    print(f"\nA média do aluno {aluno} foi {media}")