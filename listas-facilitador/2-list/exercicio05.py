"""Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] adicione o elemento 7000 logo após o elemento 6000 na lista."""

lista = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

lista[2][2].insert(2, 7000)

print(lista)