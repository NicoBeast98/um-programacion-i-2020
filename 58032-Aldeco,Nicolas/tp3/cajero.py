from billetes import *
from math import ceil


class CajeroAutomatico():
    def __init__(self):
        self.total_dinero = 0
        self.cant_billetes = [
            ['$1000', 0, 1000],
            ['$500', 0, 500],
            ['$200', 0, 200],
            ['$100', 0, 100]
        ]
        self.bill_parcial = {
            '$100' : 0,
            '$200' : 0,
            '$500' : 0,
            '$1000' : 0
        }
        self.extraccion = []

    def agregar_dinero(self, dinero):
        for bill in dinero:
            for billete in self.cant_billetes:
                if billete[0] == bill.get_rep():
                    billete[1] += 1

    def contar_dinero(self):
        for billete in self.cant_billetes:
            valor = billete[1] * billete[2]
            self.total_dinero += valor
            self.bill_parcial[billete[0]] += valor

    def extraer_dinero(self, monto, r=False):
        num = 0
        self.correct_input(monto)
        if r:
            self.cant_billetes.reverse()
        for elem in self.cant_billetes:
            if monto != 0:
                if elem[1] != 0:
                    temp = int(monto/elem[2])
                    if elem[1] < temp:
                        rg = elem[1]
                    else:
                        rg = temp
                    for i in range(rg):
                        monto -= elem[2]
                        self.cant_billetes[num][1] -= 1
                        self.bill_parcial[elem[0]] -= elem[2]
                        self.extraccion.append(elem[0])
            num += 1

    def extraer_dinero_cambio(self, monto, por):
        if (101 > por > 0) is False:
            raise Exception('El rango de porcentaje de cambio puede solo ir de 0 a 100')
        por = por/100
        cambio = self.calcular_cambio(por, monto)
        monto = monto - cambio
        self.extraer_dinero(int(monto), False)
        self.extraer_dinero(int(cambio), True)

    def correct_input(self, monto):
        if monto%100 != 0:
            raise Exception('El monto solicitado no es multiplo de 100')
        if self.total_dinero < monto:
            raise Exception(('El cajero solo tiene : {caja} y usted quiere retirar : {ext}').format(
        caja = self.total_dinero,
        ext = monto
        ))
        if self.comb(monto) is False:
            raise Exception('No hay una combinacion de billetes posible')

    def comb(self, monto):
        copy_b = self.cant_billetes
        num = 0
        m_init = monto
        test = 0
        for elem in copy_b:
            if monto != 0:
                if elem[1] != 0:
                    temp = int(monto/elem[2])
                    if elem[1] < temp:
                        rg = elem[1]
                    else:
                        rg = temp
                    for i in range(rg):
                        monto -= elem[2]
                        test += elem[2]
            num += 1
        if m_init != test:
            return False
        return True

    def calcular_cambio(self, por, monto):
        cambio = monto * por
        if cambio < 1000:
            cambio = ceil(cambio/1000)
            return cambio * 1000
        elif cambio < 10000:
            cambio = ceil(cambio/10000)
            return cambio * 1000

#   *~ Gets de datos ~*
    def get_billetes_parciales(self):
        listado = []
        for key in self.bill_parcial:
            temp = [key, self.bill_parcial[key]]
            listado.append(temp)
        return listado

    def get_cant_billetes(self):
        listado = []
        for line in self.cant_billetes:
            temp = [line[0], line[1]]
            listado.append(temp)
        return listado

    def get_total_dinero(self):
        return self.total_dinero

    def get_extra(self):
        return self.extraccion