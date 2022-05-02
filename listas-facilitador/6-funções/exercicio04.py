"""Embaralha palavras: Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados."""

from random import sample

def embaralha (string: str) -> str: 

    # Transforma uma string em uma lista, depois embaralha essa lista e transforma lista para string
    str_embaralhada = "".join(sample(string, len(string)))
    return str_embaralhada.upper()



string = input("\nDigite uma palavra, frase ou texto: ")

print(f"\nA palavra embaralhada é: {embaralha(string)}")