"""Introdução básica de dicionários"""

## Características dos dicionários 
# São estruturas de dados de mapeamento, de de-para, chave-valor
# Começam com {} e tem : que dividem as partes chave:valor e vírgula separando um par de chave e valor

from tabnanny import check

sigla_estado = {"SP" : "São Paulo", "MG" : "Minas Gerais"}
print(f"\nDicionário inicial : {sigla_estado}")

# Podemos criar um dicionário idêntico com a função dict() 
# Repare que as chaves são passadas como parâmetros nomeados da função dict(), e não como string

sigla_estado = dict(SP = "São Paulo", MG = "Minas Gerais")
print(f"\nDicionário feito pela função dict(): {sigla_estado}")

#---------------------------------------------------------------------------------------------------------#
### ACESSANDO ELEMENTOS DE UM DICIONÁRIO 

# Acessamos um valor de um dicionário a partir da sua chave usando notação de []
print(f"\nO valor para a chave 'SP' é {sigla_estado['SP']}")

# Caso a chave não exista, o código gera um erro. 
# KeyError: "RJ" -> Ela não existe no dicionário 

# Podemos criar uma chave que não existe atribuindo um valor à ela 
sigla_estado["RJ"] = "Rio de Janeiro"
print(f"\nA nova chave foi criada: {sigla_estado}")

#---------------------------------------------------------------------------------------------------------#
### MÉTODOS MAIS COMUNS DE DICIONÁRIOS 
# Alguns que não necessitam de exemplos são: clear() e copy() 
# clear() limpa o dicionário e copy() cria uma cópia dele 

# Retornando aspenas as chaves do meu dicionário
print(f"\nTransformando as chaves em uma lista: {list(sigla_estado)}") 
print(f"\nTransformando as chaves em um outro objeto: {sigla_estado.keys()} ")

# Retornando os valores do meu dicionário
print(f"\nValores do meu dicionário: {sigla_estado.values()}")

# Retornando os pares chave-valor 
print(f"\nPares de chave-valor: {sigla_estado.items()}")

#---------------------------------------------------------------------------------------------------------#

### CHECANDO EXISTENCIA DE INTES NO DICIONÁRIO
check_sp = "SP" in sigla_estado
print(f"\nA sigla SP está nas chaves? Resposta: {check_sp}")

check_se = "SE" in sigla_estado
print(f"\nA sigla SE está nas chaves? Resposta: {check_se}")