import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")

class Forma:
    def __init__(self, color, centro, nombre):
        self.color = color
        self.centro = centro
        self.nombre = nombre

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Color: {self.color}")
        print("Centro:")
        self.centro.imprimir()

    def obtenerColor(self):
        return self.color

    def cambiarColor(self, nuevo_color):
        self.color = nuevo_color

    def moverForma(self, nueva_posicion):
        self.centro = nueva_posicion

class Rectangulo(Forma):
    def __init__(self, color, centro, nombre, lado_menor, lado_mayor):
        super().__init__(color, centro, nombre)
        self.lado_menor = lado_menor
        self.lado_mayor = lado_mayor

    def imprimir(self):
        super().imprimir()
        print(f"Lado menor: {self.lado_menor}")
        print(f"Lado mayor: {self.lado_mayor}")

    def calcularArea(self):
        return self.lado_menor * self.lado_mayor

    def calcularPerimetro(self):
        return 2 * self.lado_menor + 2 * self.lado_mayor

    def cambiarTamano(self, factor):
        self.lado_menor *= factor
        self.lado_mayor *= factor

class Elipse(Forma):
    def __init__(self, color, centro, nombre, radio_mayor, radio_menor):
        super().__init__(color, centro, nombre)
        self.radio_mayor = radio_mayor
        self.radio_menor = radio_menor

    def calcularArea(self):
        return math.pi * self.radio_mayor * self.radio_menor

class Cuadrado(Rectangulo):
    def __init__(self, color, centro, nombre, lado):
        super().__init__(color, centro, nombre, lado, lado)

class Circulo(Elipse):
    def __init__(self, color, centro, nombre, radio):
        super().__init__(color, centro, nombre, radio, radio)

# Programa principal
formas = []
punto = Punto(0, 0)

rectangulo = Rectangulo("Rojo", punto, "Rectángulo", 5, 10)
formas.append(rectangulo)

elipse = Elipse("Azul", punto, "Elipse", 8, 6)
formas.append(elipse)

cuadrado = Cuadrado("Verde", punto, "Cuadrado", 7)
formas.append(cuadrado)

circulo = Circulo("Amarillo", punto, "Círculo", 5)
formas.append(circulo)

# Cambiar color y mover las formas
nuevoColor = "Cian"
nuevaPosicion = Punto(10, 10)

for forma in formas:
    forma.cambiarColor(nuevoColor)
    forma.moverForma(nuevaPosicion)
    forma.imprimir()
    print("-----")
