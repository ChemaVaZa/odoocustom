def menu():
    resposta = "dsgahahdrshbd"
    while (resposta != "1" and resposta != "2" and resposta != "3" and resposta != "0"):
        resposta = input("\n\nEscull opció:\n(1)-Majúscules\n(2)-Minúsculess\n(3)-Primera majúscula\n(0)-Sortir\nTria: ")
    return resposta

text = input("Dona'm la cadena: ")
opcio = menu()
while opcio != "0":
    if (opcio == "1"):
        print("\n",text.upper())
    elif (opcio == "2"):
        print("\n",text.lower())
    elif (opcio == "3"):
        print("\n",text.capitalize())
    opcio = menu()