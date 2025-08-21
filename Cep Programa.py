class Casa():
 #Criar Classe e definir atributos

    Imobiliaria = "Ctrl Imoveis"

    def __init__(self, Rua, bairro, Cep):
        self.rua = Rua
        self.Cep = Cep
        self.bairro = bairro
# atributos definidos
    Rua = "Blue Street"
    bairro = "Good Neighborhood"
    Cep = "123654"

    def endereçocompleto(self):
        return " Endereço Completo: " + self.Rua+ ',' +self.bairro+ " - cep" + self.Cep   
    
    def getImobiliaria(self):
        return self.Imobiliaria
    def getRua(self):
        return self.Rua
    def getbairro(self):
        return self.bairro
    def getCep(self):
        return self.Cep
    def getImobiliaria(self, i):
       self.Imobiliaria
    def getRua(self, i):
       self.Rua = i
    def getbairro(self, i):
        self.bairro = i
    def getCep(self, i):
         self.Cep = i



# Cria string para atributos
casa1 = Casa("Julio", "Nova Monte Serrat", "13299-136")
casa2 = Casa("Antonio", "Rio das Pedras", "13299-158")
casa3 = Casa("Maria", "Jd Angelicas", "13299-798")
# Print Atributos
print(casa1.endereçocompleto())
print(casa2.endereçocompleto())
print(casa3.endereçocompleto())
print(casa1.Imobiliaria)
print(casa2.Imobiliaria)
print(casa3.Imobiliaria)

casa1.setbairro('Cafezal')
print(casa1.getbairro())