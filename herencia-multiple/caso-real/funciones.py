class CASA:
    def __init__(self, pared_n, pared_s, pared_e, pared_o, ventana_n, ventana_s, ventana_e, ventana_o):
        self.pared_n = pared_n
        self.pared_s = pared_s
        self.pared_e = pared_e
        self.pared_o = pared_o
        self.ventana_n = ventana_n
        self.ventana_s = ventana_s
        self.ventana_e = ventana_e
        self.ventana_o = ventana_o

    def superficie_acristalada(self):
        suma = self.ventana_n + self.ventana_s + self.ventana_e + self.ventana_o
        return suma

    def ventanas(self):
        print("introduce la medida de la superficie de las ventanas")
        print("ventana de la pared norte:")
        self.ventana_n = input() #superficie de la ventana norte
        print("ventana de la pared sur:") 
        self.ventana_s = input()
        print("ventana de la pared este:")
        self.ventana_e = input()
        print("ventana de la pared oeste:")
        self.ventana_o = input()

