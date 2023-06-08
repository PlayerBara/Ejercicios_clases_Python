class Electrodomestico:

    def __init__(self, precio = 100.0, color = "Blanco", consumo = 'F', peso = 5.0):
        self.precioBase = precio
        self.color = color
        self.consumo = consumo
        self.peso = peso

    def getPrecioBase(self):
        return self.precioBase
    
    def setPrecioBase(self, precioBase):
        self.precioBase = precioBase
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color
    
    def getConsumoEnergetico(self):
        return self.consumo
    
    def setConsumoEnergetico(self, consumo):
        self.consumo = consumo
    
    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso
            
    def comprobarConsumoElectrico(self, letra = ""):
        if letra.upper() in ["A", "B", "C", "D", "E", "F"]:
            return letra.upper()
        else:
            return self.consumo

    def comprobarColor(self, nomColor):
        coloresDisponibles = ["blanco", "negro", "rojo", "azul", "gris"]
        if nomColor.lower() in coloresDisponibles:
            return nomColor.lower()
        else:
            return self.color

    def precioFinal(self):
        precioXConsumo = {"A": 100, "B": 80, "C": 60, "D": 50, "E": 30, "F": 10}
        precioXPeso = {0: 10, 20: 50, 50: 80, 80: 100}

        for limite, precio in precioXPeso.items():
            if self.peso <= limite:
                precio_peso = precio
                break

        return self.precioBase + precioXConsumo[self.consumo] + precio_peso
    

class Lavadora(Electrodomestico):
    cargaXDefecto = 5
    precioCarga = 50

    def __init__(self, precioBase = 50, color = "Blanco", consumoEnergetico = 'F', peso = 5, carga = 5):
        super().__init__(precioBase, color, consumoEnergetico, peso)
        self.carga = carga

    def precioFinal(self):
        precio = super().precioFinal()
        if self.carga > 30:
            precio += self.precioCarga
        return precio

class Television(Electrodomestico):
    def __init__(self, precioBase = 100, color = "blanco", consumo = 'F', peso = 5, pulgadas = 20, res4K = False):
        super().__init__(precioBase, color, consumo, peso)
        self.pulgadas = pulgadas
        self.res4K = res4K
        
    def get_pulgadas(self):
        return self.pulgadas

    def get_fourK(self):
        return self.res4K
    
    def precioFinal(self):
        precioFinal = super().precioFinal()
        if (self.pulgadas > 40):
            precioFinal *=  0.3
        elif (self.res4K == True):
            precioFinal += 50
        return precioFinal


e1 = Electrodomestico()
print(e1.precioFinal())
e2 = Lavadora()
print(e2.precioFinal())