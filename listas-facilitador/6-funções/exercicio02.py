"""Enunciado: 
Escreva uma função que, dado três comprimentos de retas quaisquer, diga se essas três retas podem ou não formar um triângulo, retornando true em caso positivo e false em caso negativo.
Dica n°1: Se algum dos comprimentos for negativo ou zero, não é possível formar um triângulo.
Dica n°2: se qualquer um dos comprimentos for maior ou igual à soma dos outros dois, então os comprimentos não podem ser usados para formar um triângulo. 
Caso contrário, eles podem formar um triângulo"""

def verifica_triangulo (lst: list) -> bool:

    triangulo = True

    if not lst:

        print("Nenhum lst encontrado para fazer o cálculo.")

    else:  

        if (lst[0] <=0 or lst[1] <= 0 or lst[2] <=0) or (
            lst[0] >= lst[1] + lst[2] or 
            lst[1] >= lst[0] + lst[2] or 
            lst[2] >= lst[0] + lst[1]): 

                triangulo = False

        else: 

            triangulo = True
        
    return triangulo


retas = []

print("\nInforme o comprimento das retas e verifique se essas formam um triângulo!")

for reta in range(3):

    reta = int(input(f"\nDigite o comprimento da reta {reta + 1} em cm: "))
    retas.append(reta)

triangulo = verifica_triangulo(retas)

print(f"\nÉ possível formar um triângulo com as retas {retas} ? {triangulo}") 

