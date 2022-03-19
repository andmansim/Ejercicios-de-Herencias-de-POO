class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    X = x
    Y = y
    
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

a = Punto2D(1,5)
print(a)

#a.traslacion(-1, -2)
#print("A = {}".format(a))