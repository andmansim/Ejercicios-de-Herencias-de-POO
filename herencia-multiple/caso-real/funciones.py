class CASA:
    def __init__(self, ventana_n, ventana_s, ventana_e, ventana_o):
        self.ventana_n = ventana_n
        self.ventana_s = ventana_s
        self.ventana_e = ventana_e
        self.ventana_o = ventana_o
        

    def superficie_acristalada(self):
        suma = int(self.ventana_n) + int(self.ventana_s) + int(self.ventana_e) + int(self.ventana_o)
        return suma





print("introduce la medida de la superficie de las ventanas")
print("ventana de la pared norte:")
v_n = input() #superficie de la ventana norte
print("ventana de la pared sur:") 
v_s = input()
print("ventana de la pared este:")
v_e = input()
print("ventana de la pared oeste:")
v_o = input()
casa = CASA(v_n, v_s, v_e, v_o)
suma = casa.superficie_acristalada()
print(suma)