import os
class Persona:
    def __init__(self, name = "Na", surname = "Na", age = 0, nie = "Na", books = []):
        self.nom = name
        self.cognom = surname
        self.edat = age
        self.dni = nie
        self.n_llibres = books

    def __str__(self) -> str:
        return f"{self.dni}"
    
    def getNom(self):
        return self.nom
    
    def getNom(self):
        return self.nom
    
    def getNom(self):
        return self.nom
    
    def getNom(self):
        return self.nom
    

class Llibre:
    def __init__(self, titol_par, autor_par, any_par):
        self.titol = titol_par
        self.autor = autor_par
        self.any = any_par

    def __str__(self) -> str:
        return self.titol
        
    def informacio(self):
        print("El llibre ", self.titol, "el va escriure ", self.autor, " l'any ", self.any)

class Biblioteca:
    def __init__(self):
        self.llibres = []
        self.persones = []
        

    def carregaLlibres(self):
            lr = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./llibres.txt"), "r+", encoding="utf-8")

            text_llibres = lr.readlines()
            
            for llibre in text_llibres:
                dades = llibre.split(":")
                self.llibres.append(Llibre(dades[0], dades[1], dades[2]))
            lr.close()

    def carregaPersones(self):
        lr = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./persones.txt"), "r+", encoding="utf-8")
        
        text_persones = lr.readlines()
        for persona in text_persones:
            dades = persona.split(":")
            self.persones.append(Persona(dades[0], dades[1], dades[2], dades[3]))
        lr.close()

    def reservaLlibres():


a = Biblioteca()
a.carregaLlibres()
a.carregaPersones()


def menu ():
    opcio = 2
    while (opcio != "0" and opcio != "1" and opcio != "2"):
        opcio = input("\n1)Reservar Llibres\n2)Tornar Llibres\n3)Llistar llibres\n4)Afegir llibre\n5)Eliminar llibre\n6)Llistar persones\n7)Afegir persones\n8)Eliminar persones\n0) Sortir del programa\n")
    return opcio


opcio = menu()
while opcio != "0":
    if (opcio == "1"):
        None
    elif (opcio == "2"):
        None
    opcio = menu()