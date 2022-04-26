"""Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

qtd_cigarros_dia = int(input("Informe a quantidade cigarros fumados por dia: "))
qtd_anos = float(input("Informe por quantos anos fumou: "))

total_cigarros = qtd_cigarros_dia * 365  * qtd_anos

tempo_perdido_minutos = total_cigarros * 10

tempo_perdido_dias = tempo_perdido_minutos / 60 * 24

print(f"\nTotal perdido de vida: {tempo_perdido_dias} dias.")