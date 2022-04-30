"""Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informadas ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04"""


atleta = input("Digite o nome do atleta: ")

notas = []

for nota in range(7):

    nota = float(input(f"Informe a nota {nota+1}: "))
    notas.append(nota)

maior_nota = max(notas)
menor_nota = min(notas)

notas.remove(maior_nota)
notas.remove(menor_nota)

media = sum(notas) / len(notas)

print("Resultado final: ")
print(f"Atleta: {atleta}")
print(f"Melhor nota: {maior_nota}")
print(f"Pior nota: {menor_nota}")
print(f"Média: {media:0.2f}")