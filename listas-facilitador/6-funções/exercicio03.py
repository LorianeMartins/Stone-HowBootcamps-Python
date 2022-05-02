"""Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721."""

def inverte_numero (numero: int) -> int:

    return int("".join(reversed(str(numero))))


numero = int(input("Digite um número inteiro: "))

print(f"O inverso desse número é {inverte_numero(numero)}")