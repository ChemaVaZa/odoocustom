class llibre:
    def __init__(self, titol_par, autor_par, any_par):
        self.titol = titol_par
        self.autor = autor_par
        self.any = any_par

    def informacio(self):
        print("El llibre ", self.titol, "el va escriure ", self.autor, " l'any ", self.any)

llib = llibre("Ubuntu", "Shuttleworth", 2014)
llib.informacio()