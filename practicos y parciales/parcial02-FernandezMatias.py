"""Tengo un negocio de venta de prendas de vestir desde hace un mes y 
quiero hacer un seguimiento de las ventas de remeras.
Toda la ropa que se vende en el negocio tiene un identificador 
(un número natural correlativo independientemente de que sea distinta prenda, 
es decir, no solo para las remeras sino para los pantalones y camisas también) 
precio y stock. Las remeras son de tamaño único y vienen en 3 colores. Todas valen $1500.
Cuando comencé con la tienda, arranqué con un stock inicial de 100 remeras de cada color.
Los colores son blanco, verde y negro.

El stock actual, almacenado por código, color y cantidad (no es obligatorio que usen esta estructura):
stock = [[7,'blanco',66], [8,'verde',12], [9, 'negro': 45]]


Quiero obtener:
El color de la remera más vendida
El monto total de facturación de remeras
Los datos de cualquier remera consultando por código"""

class Prenda:
    def __init__(self, id) -> None:
        self.id = id


class Remera(Prenda):
    def __init__(self, id, color, stock) -> None:
        super().__init__(id)
        self.color = color
        self.stock = stock
        self.cuantasVentas = 0  # Debe ser una variable de instancia
    
    def masVentas(self):
        ventas = 100 - self.stock
        if ventas > self.cuantasVentas:
            self.cuantasVentas = ventas
            self.colorMasVendido = self.color
        return f"El color de remeras más vendido es {self.colorMasVendido}"

    def facturacion(self):
        facturacion = self.cuantasVentas * 1500
        return f"El monto total de facturación fue: {facturacion}"

    def datos(self):
        return f"Los datos de la remera son: color={self.color} - stock actual={self.stock}"


stock = [[7, "blanco", 66], [8, "verde", 12], [9, "negro", 45]]

for x in stock:
    remera = Remera(*x)
    print(remera.masVentas())
    print(remera.facturacion())
    print(remera.datos())