from datetime import datetime
from logging import exception


class TRANSACCION:

    Venta = "V"
    Abastecimiento = "A"

    def __init__(self, Tipo, Cantidad):
        self.tipo = Tipo
        self.cantidad = Cantidad
        self.fecha = datetime.now()


class LIBRO:

    def __init__(self, ISBN, Titulo, Precio_compra, Precio_venta, Cantidad_actual):
        self._ISBN = ISBN
        self._titulo = Titulo
        self.precio_compra = Precio_compra
        self.precio_venta = Precio_venta
        self._cantidad_actual = Cantidad_actual
        self.transacciones = list()

    @property
    def ISBN(self):
        return self.ISBN
    
    @property
    def cantidad_actual(self):
        return self.cantidad_actual

    @cantidad_actual.setter
    def cantidad_actual(self, nuevo_valor: int):
        if nuevo_valor >= 0:
            self.cantidad_actual = nuevo_valor


class TIENDA:
    def __init__(self):
        self.Dinero_caja = 1000000
        self.catalogo = dict()

    def registrar_libro_catalogo(self, ISBN, Titulo, Precio_compra, Precio_venta, Cantidad_actual):
        if ISBN not in self.catalogo.keys():
            libro = LIBRO(ISBN, Titulo, Precio_compra, Precio_venta, Cantidad_actual)
            self.catalogo[ISBN] = libro

        else:
            raise exception("El libro ya existe en el catalogo")