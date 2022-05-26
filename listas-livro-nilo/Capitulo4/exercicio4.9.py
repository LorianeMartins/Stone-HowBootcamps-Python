"""Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O
programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O
valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação
como sendo o valor da casa a comprar dividido pelo número de meses a pagar."""

valor = float(input("Informe o valor da casa a ser comprada em R$: "))
salario = float(input("Informe o seu salário em R$: "))
anos = int(input("Informe a quantidade de anos para quitar a casa: "))
meses = anos * 12 

prestacao = valor / meses 

if prestacao > (salario * 0.3): 
    print("Empréstimo não concedido!")
else:
    print(f"O valor da prestação é de R${prestacao:0.2f} por mês.")