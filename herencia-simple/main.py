import funciones

if __name__ == "__main__":
    print("Elija dos coordenadas:")
    print("Coordenada X:")
    usuario_x = int(input())
    print("Coordenada Y:")
    usuario_y = int(input())
    a = funciones.Punto2D(usuario_x, usuario_y) #a es un objeto de la clase, nos crea las coordenadas del punto
    print("A = X: {} ; Y: {}".format(a.x, a.y))