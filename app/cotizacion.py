class Cotizacion:
    def __init__(self, cliente, ventanas):
        self.cliente = cliente
        self.ventanas = ventanas
    
    def calcular_costo_total(self):
        return sum([ventana.calcular_costo_total() for ventana in self.ventanas])
    
    def aplicar_descuento(self):
        cantidad_total = len(self.ventanas)
        if cantidad_total > 100:
            return self.calcular_costo_total() * 0.9  # Descuento del 10%
        return self.calcular_costo_total()

