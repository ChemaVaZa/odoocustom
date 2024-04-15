import random

list = ("pedra", "paper", "tisores")

opcio_ordinador = list[random.randint(0, 2)]
opcio_jugador = ""

while (opcio_jugador != list[0] and opcio_jugador != list[1] and opcio_jugador != list[2]):
    opcio_jugador = input("Pedra, paper o tisores: ")
    opcio_jugador.lower()

if (opcio_jugador == list[1]):

    if (opcio_ordinador == list[1]):
        result = "empat"
    elif (opcio_ordinador == list[0]):
        result = "victoria"
    else:
        result = "derrota"

elif (opcio_jugador == list[0]):

    if (opcio_ordinador == list[1]):
        result = "derrota"
    elif (opcio_ordinador == list[0]):
        result = "empat"
    else:
        result = "victoria"

else:

    if (opcio_ordinador == list[1]):
        result = "victoria"
    elif (opcio_ordinador == list[0]):
        result = "derrota"
    else:
        result = "empat"

print("Ordinador:", opcio_ordinador)

print(result)