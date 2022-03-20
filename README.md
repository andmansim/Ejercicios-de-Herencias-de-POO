# Ejercicios-de-Herencias-de-POO

Este trabajo se ha realizado por Ana López Palomo y Andrea Manuel Simón.
Hemos realizado distintos ejercicios de herencias, tanto simples como multiples, con sus respectivos diagramas UML.

Nuestra dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Ejercicios-de-Herencias-de-POO.git)
https://github.com/andmansim/Ejercicios-de-Herencias-de-POO.git

Primer ejercicio: Herencia simple.
Diagrama UML:

![diagrama UML herencia simple](/herencia-simple/herencia_simple.jpg)

```
import funciones

if __name__ == "__main__":
    print("Elija dos coordenadas:")
    print("Coordenada X:")
    usuario_x = int(input())
    print("Coordenada Y:")
    usuario_y = int(input())
    a = funciones.Punto2D(usuario_x, usuario_y) #a es un objeto de la clase, nos crea las coordenadas del punto
    print("A = X: {} ; Y: {}".format(a.x, a.y))
    
    print("Elija dos números que quiere sumar/restar a las coordenadas, para trasladarlo")
    print("Trasladar X")
    trasladar_x = int(input())
    print("Trasladar Y")
    trasladar_y = int(input())
    a.traslacion(trasladar_x, trasladar_y)
    print("A = X: {} ; Y: {}".format(a.x, a.y))
    
    #Lo mismo que antes pero con tres coordenadas
    print("Ahora elija tres coordenadas:")
    print("Coordenada X:")
    usuario1_x = int(input())
    print("Coordenada Y:")
    usuario1_y = int(input())
    print("Coordenada Z:")
    usuario1_z = int(input())
    b = funciones.Punto3D(usuario1_x, usuario1_y, usuario1_z)
    print("B = X: {} ; Y: {} ; Z: {} ".format(b.x, b.y, b.z))
    
    print("Elija tres números que quiere sumar/restar a las coordenadas, para trasladarlo")
    print("Trasladar X")
    trasladar1_x = int(input())
    print("Trasladar Y")
    trasladar1_y = int(input())
    print("Trasladar Z")
    trasladar1_z = int(input())
    b.traslacion1(trasladar1_x, trasladar1_y, trasladar1_z)
    print("B = X: {} ; Y: {} ; Z: {} ".format(b.x, b.y, b.z))
    
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
```

En el segundo ejercicio hemos tenido que responder a una pregunta, cuya respuesta es la siguiente:
```
#Este programa en la salida estandar muestra:
'''
a
b
bb
bb
c
cc
c
'''
```
Los siguientes ejercicios son de herencia múltiple, el primero es diamante-argumentos.
Su diagrama UML es el siguiente:

![diagrama UML herencia simple](/herencia-multiple/diamante-argumentos/diamante.jpg)

```
import funciones
if __name__ == "__main__":
    d = funciones.D(1, 2, 3)
    print(isinstance(d, funciones.A),isinstance(d, funciones.B),isinstance(d, funciones.C))
    print(d.a, d.b, d.c)    
    
class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b
        
class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)
        self.c = c

class D(B, C):
    def __init__(self, a, b, c):
        B.__init__(self, a, b)
        C.__init__(self, a, c)
```

El segundo es diamante-argumentos.
Su diagrama UML es el siguiente:

![diagrama UML herencia simple](/herencia-multiple/diamanteargumentos.jpg)


