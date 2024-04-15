import os
def menu():
    file_a = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./a.txt"), "r+", encoding="utf-8")
    file_b = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./b.txt"), "r+", encoding="utf-8")

    resposta = ""
    while (resposta != "0" and resposta != "1" and resposta != "2" and resposta != "3"):
        resposta = input("\n\nEscull opció:\n(1)-Comptar línies\n(2)-Comptar paraules\n(3)-Comptar caràcters\n(0)-Sortir\n")

    if (resposta == "1"):
        linies = file_a.readlines()
        print("Arxiu a:", len(linies))
    
        linies = file_b.readlines()
        print("Arxiu b:", len(linies))

    elif (resposta == "2"):
        linies = file_a.readlines()

        cont_parau = 0
        for linia in linies:
            paraules = linia.split()
            cont_parau += len(paraules)

        print("Arxiu a:", cont_parau)

        linies = file_b.readlines()

        cont_parau = 0
        for linia in linies:
            paraules = linia.split()
            cont_parau += len(paraules)

        print("Arxiu b", cont_parau)

    elif (resposta == "3"):
        linies = file_a.readlines()
        cont_character = 0
        for linia in linies:
            for character in linia:
                if (character != " "):
                    cont_character += 1

        print("Arxiu a:", cont_character)

        linies = file_b.readlines()
        cont_character = 0

        for linia in linies:
            for character in linia:
                if character != " ":
                    cont_character += 1

        print("Arxiu b:", cont_character)

    else:
        file_a.close()
        file_b.close()

    return resposta

resposta = 2
while resposta != "0":
    resposta = menu()