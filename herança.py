class animalselvagem():
    def __init__(self):
        print("Animal criado")

    def mover(self):
            print("estou correndo")

    def come(self):
         print("Comendo")
class animaldomestico():
    def mover():
         print("estou andando")   
    def getdono(self):
         return self.dono

class Cachorro(animalselvagem, animaldomestico):
    def __init__(self, dono):
        self.dono = dono


    def late(self):
        print("AUau!")
                   
c = Cachorro("Luis")
print(c.getdono())
c.come()
c.late()
c.mover()


