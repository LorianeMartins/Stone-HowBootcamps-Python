"""Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado."""
from tabnanny import check


estado_sigla = {
    "RR": "Roraima",
    "AP": "Amapá",
    "AM": "Amazonas",
    "PA": "Pará",
    "AC": "Acre",
    "RO": "Rondônia",
    "TO": "Tocantins",
    "MA": "Maranhão",
    "PI": "Piauí",
    "CE": "Ceará",
    "RN": "Rio Grande do Norte",
    "PB": "Paraíba",
    "PE": "Pernambuco",
    "AL": "Alagoas",
    "SE": "Sergipe",
    "BA": "Bahia",
    "MT": "Mato Grosso",
    "DF": "Distrito Federal",
    "GO": "Goiás",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "ES": "Espírito Santo",
    "RJ": "Rio de Janeiro",
    "SP": "São Paulo",
    "PR": "Paraná",
    "SC": "Santa Catarina",
    "RS": "Rio Grande do sul",
}

sigla_informada = input("Informe a sigla do estado: ").upper()

if sigla_informada in estado_sigla: 
    print(f"\nEstado referente a sigla {sigla_informada}: {estado_sigla[sigla_informada]}")
else: 
    input("Sigla inválida.") 
    