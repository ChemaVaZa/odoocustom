import os
class Persona:
    def __init__(self, name = "Na", surname = "Na", age = 0, nie = "Na", books = []):
        self.nom = name
        self.cognom = surname
        self.edat = age
        self.dni = nie
        self.n_llibres = books

    def getNom(self):
        return self.nom
    
    def getCognom(self):
        return self.cognom
    
    def getEdat(self):
        return self.edat
    
    def getDNI(self):
        return self.dni
    
    def getNLlibres(self):
        return self.n_llibres

    def __str__(self) -> str:
        return f"{self.dni}"

    def reserva(self):
        self.n_llibres
        return self.cognom

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
    
    def reservaLlibre(self, dni, n_llibre):
        dni += "\n"
        for i in range(0, len(self.persones)):
            for j in range(0, len(self.llibres)):
                if (print(self.persones[i]) == dni):
                    


        #pw = open (os.path.join(os.path.dirname(os.path.realpath(__file__)), "./persones.txt"), "w+", encoding="utf-8")
        nouText = ""
        for text in text_persones:
            nouText += text
        #pw.write(nouText)
        
    def llistaLlibresDNI(self, dni):
        #lr = open (os.path.join(os.path.dirname(os.path.realpath(__file__)), "./llibres.txt"), "r+", encoding="utf-8")
        #text_llibres = lr.readlines()
        cont = 0
        text_llibres = self.llibres
        for llibre in text_llibres:
            dades = llibre.split(":")
            if (dades[4] == dni):
                print("\n" , cont , ")" , llibre)
                cont += 1
        #lr.close()
    
    def llistaLlibres(self):
        lr = open (os.path.join(os.path.dirname(os.path.realpath(__file__)), "./llibres.txt"), "r+", encoding="utf-8")
        cont = 0
        for llibre in self.llibres:
            print("\n" , cont , ")" , llibre.informacio())
            cont += 1
        lr.close() 
        return input("Quin llibre vols? (número)")


def obtenirPersones():
    pr = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./persones.txt"), "r+", encoding="utf-8")
    text_persones = pr.readlines()
    persones = []
    for persona in text_persones:
        dades = persona.split(":")
        persones.append(Persona(dades[0], dades[1], dades[2], dades[3] ,dades[4]))
    pr.close()
    return persones

def obtenirLlibres():
    None

def menu ():
    opcio = 2
    while (opcio != "0" and opcio != "1" and opcio != "2"):
        opcio = input("\n1)Reservar Llibres\n2)Tornar Llibres\n0) Sortir del programa\n")
    return opcio





#pw = open (os.path.join(os.path.dirname(os.path.realpath(__file__)), "./persones.txt"), "a+", encoding="utf-8")
#lw = open (os.path.join(os.path.dirname(os.path.realpath(__file__)), "./llibres.txt"), "a+", encoding="utf-8")
#lr = open (os.path.join(os.path.dirname(os.path.realpath(__file__)), "./llibres.txt"), "r+", encoding="utf-8")
#pr = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./persones.txt"), "r+", encoding="utf-8")

persones = obtenirPersones()
llibres = obtenirLlibres()
biblioteca = Biblioteca()
biblioteca.carregaPersones()
biblioteca.carregaLlibres()
biblioteca.reservaLlibre("2","s")
opcio = menu()
while opcio != "0":
    if (opcio == "1"):
        n_llibre = llistaLlibres()
        dni = input("Quin és el teu dni? ")
        biblioteca.reservaLlibre(dni, n_llibre)
    elif (opcio == "2"):
        None
    opcio = menu()