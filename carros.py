class Carros():
 #Criar Classe e definir atributos

    def __init__(self,marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def carrovolks(self):
        return " Marca do carro : " + self.marca+ ' Modelo: ' +self.modelo+ " Ano: " + self.ano   
    

carro1 = Carros("Volkswagen", "Gol", "10")
carro2 = Carros("Volkswagen", "Amarok", "3")
print(carro1.carrovolks())
print(carro2.carrovolks())