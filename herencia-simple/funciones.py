class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def traslacion(self, a, b):
        self.x = self.x + a
        self.y = self.y + b
        return self.x, self.y

class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def traslacion(self, a, b, c):
        self.x = self.x + a
        self.y = self.y + b
        self.z = self.z + c

a = Punto2D(1,5) #a es un objeto de la clase, nos crea las coordenadas del punto

print(a.x,a.y)
print("A = {}".format(a.y))


print(a.traslacion(-1, -2))