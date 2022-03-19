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
    
    def traslacion1(self,a, b, c):
        self.x = self.x + a
        self.y = self.y + b
        self.z = self.z + c
        return self.x, self.y, self.z

b = Punto3D(2, 5, 7)
print("B = X: {} ; Y: {} ; Z: {} ".format(b.x, b.y, b.z))
b.traslacion1(1, 3, 2)
print("A = X: {} ; Y: {}; Z: {} ".format(b.x, b.y, b.z))