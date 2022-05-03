
from random import choice, randint

import cartela

# Passo 2:
def sorteia(): 

   letra_sorteada = choice(cartela.LETRAS)
   #letra_sorteada = "G"

   minimo, maximo = cartela.min_max(letra_sorteada)

   numero_sorteado = randint(minimo, maximo)
   #numero_sorteado = 60

   print(f"A combinação sorteada foi {letra_sorteada}{numero_sorteado}")

   return letra_sorteada, numero_sorteado


