"""Estrutura condicional(if, else, elif)"""

aluna = "Loriane Martins"

# Criando uma lista vazia 
notas = []

# Adicionando a primeira nota à lista
notas.append(float(input("Digite a primeira nota: ")))

# Adicionando a segunda nota à lista
notas.append(float(input("Digite a segunda nota: ")))

# Adicionando a terceira nota à lista
notas.append(float(input("Digite a terceira nota: ")))

nota_media = sum(notas) / len(notas)

# Definindo padrões de aprovação 
nota_minima_aprovacao = 7 
nota_minima_rec = 6 

# Verificação de aprovação do aluno 
if nota_media >= nota_minima_aprovacao:
    status = "aprovado(a)"

# Verificação de reprovação ou recuperação, caso o aluno não tenha sido aprovado 
elif nota_media >= nota_minima_rec:
    
    ## Chance de eliminar a nota mais baixa 

    # Menor nota do aluno
    menor_nota = min(notas)

    # Índice da menor nota na lista
    indice_menor_nota = notas.index(menor_nota)

    # Eliminando a menor nota pelo índice
    notas.pop(menor_nota)

    # Recalcula a média 
    nota_media = sum(notas) / len(notas)

    if nota_media >= nota_minima_aprovacao: 
        status = f"aprovado(a) com {len(notas)}"
    else:
        status = "recuperação"
#Se nenhuma das condições acima foi satisfeita, então o aluno está reprovado! 
else:
    status = "reprovado(a)"      

# Arrendondando a média para 2 casas decimais
nota_media_arred = round(nota_media, 2)

#Imprime o resultado final na tela 
print(f"\nA média do aluno(a) {aluna} é {nota_media_arred} e este aluno(a) tem o seguinte status: {status}")


