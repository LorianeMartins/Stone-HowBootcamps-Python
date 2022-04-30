"""Um determinado zoológico cobra a entrada com base na idade do visitante.
Os visitantes com 2 anos de idade ou menos não pagam para entrar.
Crianças entre 3 e 12 anos custa R$14,00.
Idosos com 65 anos ou mais custam R$18,00.
A entrada para todos os outros visitantes é de R$23,00.
Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, com uma idade inserida em cada linha.
O usuário digitará uma linha em branco para indicar que não há mais visitantes no grupo.
Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada.
O custo deve ser exibido usando duas casas decimais."""


valores = []

print("Digite as idades para adicionar integrantes ao grupo...")
print("... ou pressione enter para deixar em branco e encerrar!")

while "" not in valores: 

    idade = input("Informe a idade do visitante em anos: ")

    if idade != "" and idade.isdigit():

        idade = int(idade)
        
        if idade <= 2: 
            custo = 0
        
        elif 3 <= idade <= 12: 
            custo = 14.00
    
        elif 12 < idade < 65: 
            custo = 23.00
    
        else: 
            custo = 18.00

        valores.append(custo)

    else:
        break

if not valores: 
    print(f"Não foi encontrado nenhum valor.")

else:
    preco_total = sum(valores)
    print(f"O preço total dos ingressos é de R${preco_total:0.2f}")

