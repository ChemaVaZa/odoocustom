class Llibre:
    def __init__(self, titol_par, autor_par, any_par):
        self.titol = titol_par
        self.autor = autor_par
        self.any = any_par

    def informacio(self):
        print("El llibre ", self.titol, "el va escriure ", self.autor, " l'any ", self.any)

lli = open("M10_UF2_Pt3_Vazquez/llibres.txt", "r+")

llibres = lli.readlines()
llista_llibres = [None] * len(llibres)
cont = 0
for llibre in llibres:
    dades = llibre.split(":")
    llista_llibres[cont] = Llibre(dades[0], dades[1], dades[2])
    print(Llibre(dades[0], dades[1], dades[2]).informacio())
    cont += 1
