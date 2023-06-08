from random import randint

class Persona:

    #parte 6 / 6
    #generaDNI(): este metodo sera convocado cuando se cree el objeto
    def generarDNI(self):
        numbers = randint(10000000, 99999999)
        letter = "TRWAGMYFPDXBNJZSQVHLCKET"
        DNI = str(numbers) + letter [numbers % 23]
        return DNI
    
    #Parte 1 / 6 OK
    def __init__(self, nombre = "", edad = 0, sexo = 'M', peso = 1.0, altura = 1.0):
        self.nombre = nombre #No obligatorio
        self.edad = int(edad) #No obligatorio
        self.DNI = self.generarDNI() #Obligatorio
        self.sexo = sexo #Por defecto el sexo es mujer
        self.peso = float(peso)
        self.altura = float(altura)

    #Parte 2 / 6 OK
    def calcularIMC(self):
        aux = self.peso/(self.altura * self.altura)
        return aux
    
    def pesoIdeal(IMC):
        pesoIdeal = 0

        if IMC < 18.5:
            pesoIdeal = -1

        if IMC > 25:
            pesoIdeal = 1
        
        return pesoIdeal
    
    #Parte 3 / 6 OK
    def esMayorDeEdad(self):
        mayor = False
        if self.edad > 18:
            mayor = True
        return mayor

    #Parte 4 / 6 OK
    def introducirSexo(self, sexo):
        self.sexo = sexo

    #Parte 5 / 6 OK
    def __str__(self):
        text = "Nombre: " + self.nombre + "\nEdad: " + str(self.edad) + "\nDNI: " + self.DNI + "\nSexo: " + self.sexo + "\nPeso: " + str(self.peso) + "\nAltura: " + str(self.altura)
        return text
    
    

nombre = input("Introduce el nombre: ")
edad = input("Introduce la edad: ")
sexo = input("Introduce el sexo: ")
peso = input("Introduce el peso: ")
altura = input("Introduce la altura: ")
    
persona1 = Persona (nombre, edad, sexo, peso, altura)

print(persona1)
print(persona1.calcularIMC())
print(persona1.esMayorDeEdad())


persona2 = Persona (nombre, edad, sexo)

print(persona2)
print(persona2.calcularIMC())
print(persona2.esMayorDeEdad())

pepe = Persona("Pepe", 26, 'M', 99.8, 1.89)

print(pepe)
print(pepe.calcularIMC())
print(pepe.esMayorDeEdad())