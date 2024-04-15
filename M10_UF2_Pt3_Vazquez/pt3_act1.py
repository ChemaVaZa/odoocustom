class compteBancari:
    def __init__(self, nom, diners):
        self.titular = nom
        self.saldo = diners

    def ingressar(self, diners):
        self.saldo += diners

    def retirar(self, diners):
        self.saldo -= diners

compte = compteBancari("Anna", 100)
print(compte.saldo) 
print(compte.titular) 

compte.ingressar(50)
print(compte.saldo) 

compte.retirar(25)
print(compte.saldo) 
