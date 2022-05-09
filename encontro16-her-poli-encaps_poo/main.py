""" POO - introdução """

from pessoas import Funcionario

funcionario1 = Funcionario("João", "Silva", 5000)

funcionario2 = Funcionario("Loriane", "Moreira Martins", 5500)

funcionario3 = Funcionario("Sérgio", "Ramos", 4500)

funcionario1._salario_inicial = 10000

funcionario1.dar_aumento()

print(funcionario1.salario_atual)