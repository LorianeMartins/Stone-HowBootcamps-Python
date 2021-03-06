"""Faça um programa que responda as seguintes perguntas:
1.	Quantos alunos estão matriculados na escola, no total?
2.	Quantos e quais estão matriculados APENAS em INGLES?
3.	Quantos e quais estão matriculados APENAS em FRANCES?
4.	Quantos e quais estão matriculados EM AMBOS os cursos?
5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
"""
alunos_ingles = {
    "João Alves dos Santos",
    "Maria Magalhães",
    "Antônio da Silva Ferreira",
    "José Júnior Jarbas",
    "Henrique da Silva Sauro",
    "Joaquina Ferreira da Silva",
    "Fabiana Aparecida Bianco",
    "Marrone Gutierres",
    "Carlos Magno Farad",
    "Antônio da Silva Júnior Amaral",
}

alunos_frances = {
    "João Alves dos Santos",
    "Antônio da Silva Ferreira",
    "Fernanda Abdala Mohamed",
    "Abner Mignon Alib",
    "Alisson Figueiredo",
    "Henrique da Silva Sauro",
    "Maria Magalhães",
    "Marrone Gutierres",
    "Joaquina Ferreira da Silva",
}

print(f"\nTotal de alunos matriculados na escola: {len(alunos_ingles.union(alunos_frances))}")
print(f"\nTotal de alunos matriculados apenas em INGLÊS: {len(alunos_ingles - alunos_frances)}. Os alunos são:\n{(alunos_ingles - alunos_frances)} ")
print(f"\nTotal de alunos matriculados apenas em INGLÊS: {len(alunos_frances - alunos_ingles)}. Os alunos são:\n{(alunos_frances - alunos_ingles)} ")
print(f"\nTotal de alunos matriculados em INGLÊS e FRANCÊS: {len(alunos_frances.intersection(alunos_ingles))}. Os alunos são:\n{(alunos_frances.intersection(alunos_ingles))} ")
print(f"\nTotal de alunos matriculados ou INGLÊS ou FRANCÊS, mas não em AMBOS: {len(alunos_frances.symmetric_difference(alunos_ingles))}")