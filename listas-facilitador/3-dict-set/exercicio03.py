"""Faça um programa que ordene um dicionário por seus valores
dict_to_order = {"matemática": 81, "física": 83, "química": 87}"""

dict_to_order = {"matemática" : 81, "física": 83,  "química" : 87}

## Dicionários não possuem o método sort(). 
## Nesse caro, para usar o sorted() é preciso passar alguns argumentos. Está na documentação. 
## Primeiro, é preciso tranformar o dicionário para tuplas a fim de pegar o segundo valor da tupla, que é a nota para ordenar. 

# Método que retorna uma lista de tuplas com a chave-valor. 
# dict_to_order.items()
# `key` precisa ser uma função, pois ela quem define como será ordenado. 
# Função `lambda` é uma função anônima que pega o segundo elmento da tupla. 
# Reverse é pra dizer se será ordenado de forma crescente ou decrescente. 
# Como a função sorted retornará uma lista de tuplas, é preciso converter para dicionário novamente. 

novo_dicionario = dict((sorted(dict_to_order.items(), key= lambda tupla: tupla[1], reverse = True)))

print(novo_dicionario)

#Outra forma de fazer: usar o .get, pois esse método retorna o valor da chave
for chave in sorted(dict_to_order, key = dict_to_order.get, reverse= True):
    print(chave, dict_to_order[chave])
