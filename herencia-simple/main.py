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
    
    