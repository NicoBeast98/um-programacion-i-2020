# Billetes
class Billete():
    def __init__(self):
        self.valor = None
        self.moneda = None
        self.representacion = None

    def get_valor(self):
        return self.valor

    def get_moneda(self):
        return self.moneda

    def get_rep(self):
        return self.representacion

class Bill_100(Billete):
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.valor = 100
        self.moneda = 'pesos'
        self.representacion = '$100'

class Bill_200(Billete):
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.valor = 200
        self.moneda = 'pesos'
        self.representacion = '$200'


class Bill_500(Billete):
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.valor = 500
        self.moneda = 'pesos'
        self.representacion = '$500'


class Bill_1000(Billete):
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.valor = 1000
        self.moneda = 'pesos'
        self.representacion = '$1000'