import math

class FiguraGeometrica:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return 3 * self.base

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi * (self.raio ** 2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.raio

retangulo = Retangulo(4, 5)
triangulo = Triangulo(3, 6)
circulo = Circulo(2)

print("Área e Perímetro do Retângulo:")
print("Área:", retangulo.calcularArea())
print("Perímetro:", retangulo.calcularPerimetro())

print("\nÁrea e Perímetro do Triângulo:")
print("Área:", triangulo.calcularArea())
print("Perímetro:", triangulo.calcularPerimetro())

print("\nÁrea e Perímetro do Círculo:")
print("Área:", circulo.calcularArea())
print("Perímetro:", circulo.calcularPerimetro())
