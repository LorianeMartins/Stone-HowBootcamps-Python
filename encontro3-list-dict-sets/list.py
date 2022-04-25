"""Introdução básica de listas"""

##Listas começam com []
notas = [4, 5, 0, 9, 10]
print(f"\nNotas: {notas}")

##Podemos transformar outros objetos para o tipo de lista com a função list()
notas_tup = (1, 2, 3, 4)
notas = list(notas_tup)
print(f"\nO tipo da variável notas é: {type(notas)}")

##Uma lista pode armazenar vários tipos de objetos
list_obj_variados = ["Loriane", 1, 10.0, False, [5,5,5]]
print(f"\nLista com tipos de objetos variados: {list_obj_variados}")

##Comprimento da lista
print(f"\nA lista `list_obj_variados` tem {len(list_obj_variados)} elementos")

#-----------------------------------------------------------------------------#
### ACESSANDO ELEMENTOS DE LISTTA COM FATIAMENTO (SLICING)

#########################################
# INDEXAÇÃO EM PYTHON COMEÇA POR ZERO !!!
#########################################

# Acessando o primeiro elemento da lista 
primeiro_elemento = list_obj_variados[0]
print(f"\nO primeiro elemento da lista é {primeiro_elemento}")

segundo_elemento = list_obj_variados[1]
print(f"\nO segundo elemento da lista é {segundo_elemento}")

#A indexação também pode ser na ordem inversa(da direita para esquerda)
#Basta passar números negativos 
ultimo_elemento = list_obj_variados[-1]
penultimo_elemento = list_obj_variados[-2]
print(f"\nO último elemento da lista é {ultimo_elemento} e o penúltimo é {penultimo_elemento}")

#----------------------------------------------------------------------------------------------#
### MÉTODOS MAIS COMUNS DE LISTAS 

# Adicionando elemento no final da lista
list_obj_variados.append([9, 9, 9])
print(f"\nO elemento [9, 9, 9] foi adicionado ao final da lista: {list_obj_variados}")

# Adicionando elemento a elemento de um objeto à lista 
list_obj_variados.extend("Loriane Martins")
print(f"\nCada letra da string foi adicionada como um elemento à lista: {list_obj_variados}")

# Adicionando um objeto inteiro em uma determinada posição
list_obj_variados.insert(0, "Index 0")
print(f"\nA string foi adicionada na primeira posição da lista, de índice 0: {list_obj_variados}")

# Removendo o primeiro elemento encontrado da lista, retorna erro se não encontrar o elemento
list_obj_variados.remove([9, 9, 9])
print(f"\nO objeto [9, 9, 9] agora foi removido da lista: {list_obj_variados}")

# Coletando um elemento da lista e salvando em uma variável a partir de um índice
# O .pop() permite salvar o elemento removido de uma variável, o .remove() não permite! 
elemento_coletado = list_obj_variados.pop(0)
print(f"\nO elemento do índice 0 foi removido da lista: {list_obj_variados}")
print(f"\nO elemento coletado é {elemento_coletado}")

# Ordenando os valores de uma lista 
notas.sort()
print(f"\nNotas ordenadas: {notas}")

# temos ainda os métodos .clear(), .copy(), .reverse()
