"""Introdução básica de set"""

## Característica dos sets: 
# Conjuntos matemáticos 
# Não há como acessar por posição 
# Elementos únicos, exclusivos, sem repetição 

# Formas de se criar um set
# Usando a notação {}
# Percebam que é diferente de um dicionário, pois dict tem {} e :, separando as chaves e valores
conjunto_a = {1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4}
print(f"\nConjunto A: {conjunto_a}")

# Podemos usar a função set() para transformar outros objetos em um set 
aluna = set("Loriane Martins")
letras_aleatorias = set("HeinbfnAs ")

#------------------------------------------------------------------------------------------------# 
### COMPARANDO CONJUNTOS 

# Pergunta 1: Quais letras em comum temos em `aluna` e `letras_aleatorias` ? 
print(f"Resp : {aluna.intersection(letras_aleatorias)}")

# Pergunta 2: Quais letras temos em `aluna` que não estão em `letras_aleatorias` ? 
print(f"Resp 2: {aluna - letras_aleatorias}")

# Pergunta 3: Quais letras temos em `letras_aleatorias` que não estão em `aluna` ? 
print(f"Resp 3: {letras_aleatorias - aluna}")

# Pergunta 4: Quantas letras não repetidas temos ao total, quando consideramos `aluna` e `letras_aleatorias` ? 
print(f"Resp 4: {len(aluna.union(letras_aleatorias))}")

# Pergunta 5: Quais letras estão ou em `letras_aleatorias` ou em `aluna`
print(f"Resp 5: {aluna.symmetric_difference(letras_aleatorias)}")

# Pergunta 6: A letra a está em `aluna` ? 
print(f"Resp 6: {'a' in aluna}")

# Pergunta 7: `letras_aleatorias` é um subconjunto de `aluna` ? 
print(f"Resp 7: {letras_aleatorias.issubset(aluna)}")

# pensou em conjunto, comparações, pensou em sets!!!


