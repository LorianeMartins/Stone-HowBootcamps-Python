"""Introdução aos tipos de dados (int, float)"""

aluno = "Loriane M Martins"

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3 

media_arred = round(media, 2)

print(f"\nA média do aluno {aluno} é {media_arred}")
