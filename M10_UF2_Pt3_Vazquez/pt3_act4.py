import os

def menu ():
    opcio = 2
    while (opcio != "0" and opcio != "1" and opcio != "2" and opcio != "3"):
        opcio = input("\n1)Llistar Llibres\n2)Introduir Llibres\n3)Eliminar  Llibres\n0) Sortir del programa\n")
    return opcio

def llistar():
    text = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./llibres.txt"), "r+", encoding="utf-8")
    llibres = text.readlines()

    for llibre in llibres:
        dades = llibre.split(":")
        print("El llibre " , dades[0] , " el va escriure " , dades[1] , " l'any " , dades[2].rstrip("\n"))
    text.close()

def introduir():
    text_escriure = open("M10_UF2_Pt3_Vazquez/llibres.txt", "a+")

    nom = input("Nom del llibre: ")
    autor = input("Autor del llibre: ")
    any = input("Any de creació del llibre: ")
    nou_llibre ="\n" + nom + ":" + autor + ":" + any
   
    text_escriure.write(nou_llibre)
    print("Llibre afegit")

    text_escriure.close()
    
def eliminar():
    text_llegir = open("M10_UF2_Pt3_Vazquez/llibres.txt", "r+")
    
    llibres = text_llegir.readlines()
    cont = 0
    for llibre in llibres:
        dades = llibre.split(":")
        print(cont , ") El llibre " , dades[0] , " el va escriure " , dades[1] , " l'any " , dades[2])
        cont += 1
    linia_eliminada = int(input("Escull el llibre que vulguis eliminar: "))
    llibres.pop(linia_eliminada)
    
    text_llibres = ""
    for llibre in llibres:
        text_llibres += llibre

    text_escriure = open("M10_UF2_Pt3_Vazquez/llibres.txt", "w+")
    text_escriure.write(text_llibres)
    
    text_escriure.close()
    text_llegir.close()
    print("Llibre eliminat")
    

opcio = menu()
while opcio != "0":
    if (opcio == "1"):
        llistar()
    elif (opcio == "2"):
        introduir()
    elif (opcio == "3"):
        eliminar()
    opcio = menu()