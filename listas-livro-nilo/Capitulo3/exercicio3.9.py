"""Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos."""

dias = int(input("Informe a quantidade de dias: "))
horas = float(input("Informe a quantidade de horas: "))
minutos = float(input("Informe a quantidade de minutos: "))
segundos = float(input("Informe a quantidade de segundos: "))

total_em_segundos = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print(f"\nTotal em segundos: {total_em_segundos}")