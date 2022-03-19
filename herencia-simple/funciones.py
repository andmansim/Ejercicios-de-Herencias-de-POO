class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def traslacion(self, a, b):
        self.x = self.x + a
        self.y = self.y + b
        return self.x, self.y

class Punto3D(Punto2D):
    def __init__(self,z):
        self.z = z
    
    def traslacion(self, a, b, c):
        self.x = self.x + a
        self.y = self.y + b
        self.z = self.z + c

a = Punto2D(1,5) #a es un objeto de la clase, nos crea las coordenadas del punto
print("A = X: {} ; Y: {}".format(a.x, a.y))

a.traslacion(-1, -2)
print("A = X: {} ; Y: {}".format(a.x, a.y))