"""
Enunciado: 
Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). Imprima na tela o elemento e sua respectiva posição na lista. """

lista_variada = [1.0, "Loriane", 10, [5, 5, 5], "Martins"]

lista_posicao_elemento = list(enumerate(lista_variada))

print(f"A posição e o respectivo elemento da lista estão representados a seguir:\n{lista_posicao_elemento}")

