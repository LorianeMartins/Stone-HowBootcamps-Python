"""Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves."""

entrada = {"Theodoro": 20, "Márcia": 50, "Júnior": 80} 

valores = list(entrada.values())
maior_valor = max(valores)
menor_valor = min(valores)

index_maior_nota = valores.index(maior_valor)
index_menor_nota = valores.index(menor_valor)

chaves = list(entrada.keys())

print(f"\nNota máxima -> {chaves[index_maior_nota]}: {maior_valor}")
print(f"Nota mínima -> {chaves[index_menor_nota]}: {menor_valor}")