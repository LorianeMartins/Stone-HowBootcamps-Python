class Imposto:
    def calcula(self):
        pass

    def __str__(self):
        return "Print da classe imposto"
    
    def __repr__(self): 
        return "Representação da classe imposto"

class ICMS(Imposto):
    def calcula(self, valor_bruto):
        return valor_bruto * (1 - 0.05) 

class IPI(Imposto):
    def calcula(self, valor_bruto):
        return valor_bruto * (1 - 0.15) 

class ISS(Imposto):
    def calcula(self, valor_bruto):
        return valor_bruto * (1 - 0.10) 

class COFINS(Imposto):
    def calcula(self, valor_bruto):
        return valor_bruto * (1 - 0.03)