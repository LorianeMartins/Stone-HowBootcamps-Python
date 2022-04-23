"""Métodos de string com a sintaxe nome.metodo()"""

nome = " Loriane Moreira Martins "

print(f"Nome em maiúsculo: {nome.upper()}")

print(f"Nome em minúsculo: {nome.lower()}")

print(f"Primeira letra em maiúsculo: {nome.capitalize()}")

print(f"Contando quantas vezes a letra 'a' aparece no nome: {nome.count('a')}")

print(f"Removendo espaços em branco no começo e final da string: {nome.strip()}")

print(f"Substituindo meu nome por algo engraçado: {nome.replace('Loriane', 'hair')}")

print(f"Separando o nome em partes: {nome.split()}")

print(f"A minha string contém {len(nome)} caracteres(considerando os espaços em branco)")
