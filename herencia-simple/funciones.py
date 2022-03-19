class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def traslacion(self, a, b):
        self.x = self.x + a
        self.y = self.y + b
        return self.x, self.y

class Punto3D(Punto2D):
    def __init__(self, x, y, z):
    
        Punto2D.__init__(self, x, y) #cogemos el constructor de la clase base
        self.z = z
    
    def traslacion(self, c):
        self.z = self.z + c

a = Punto2D(1,5) #a es un objeto de la clase, nos crea las coordenadas del punto
print("A = X: {} ; Y: {}".format(a.x, a.y))

a.traslacion(-1, -2)
print("A = X: {} ; Y: {}".format(a.x, a.y))

b = Punto3D(2, 5, 7)
print("B = X: {} ; Y: {} ; Z: {} ".format(b.x, b.y, b.z))
b.traslacion(1, 3, 2)
print("A = X: {} ; Y: {}; Z: {} ".format(b.x, b.y, b.z))