import funciones

if __name__ == "__main__":
    #calculo de las ventanas
    funciones.proteccion()
    print("introduce la medida de la superficie de las ventanas")
    print("ventana de la pared norte:")
    v_n = input()
    print("ventana de la pared sur:") 
    v_s = input()
    print("ventana de la pared este:")
    v_e = input()
    print("ventana de la pared oeste:")
    v_o = input()

    casa = funciones.CASA(v_n, v_s, v_e, v_o)
    suma = casa.superficie_acristalada()
    print("Esta es la superficie total de las ventanas: " + str(suma))

    #calculo de las paredes cortina
    print("introduce la medida de la superficie de las paredes cortina")
    print("cortina norte:")
    c_n = input()
    print("cortina sur:") 
    c_s = input()
    print("cortina este:")
    c_e = input()
    print("cortina oeste:")
    c_o = input()

    paredes_cortina = funciones.CASA(c_n, c_s, c_e, c_o)
    suma = paredes_cortina.superficie_acristalada()
    print("Esta es la superficie total de las paredes cortina: " + str(suma))