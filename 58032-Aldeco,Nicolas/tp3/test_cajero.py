#! /usr/bin/python3
import unittest
from cajero import *


# Solo billetes de $1000
class TestCajero1(unittest.TestCase):

    def setUp(self):
        self.value = CajeroAutomatico()
        self.value.agregar_dinero([
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
            Bill_1000(),
        ])
        self.value.contar_dinero()

    def test_1_contar_dinero_parciales(self):
        temp = self.value.get_billetes_parciales()
        self.assertEqual(
            temp, [['$100', 0], ['$200', 0], ['$500', 0], ['$1000', 10000]])

    def test_2_contar_billetes(self):
        temp = self.value.get_cant_billetes()
        self.assertEqual(
            temp, [['$1000', 10], ['$500', 0], ['$200', 0], ['$100', 0]])

    def test_3_total_dinero(self):
        total = self.value.get_total_dinero()
        self.assertEqual(total, 10000)

    def test_4_extraer_5000(self):
        self.value.extraer_dinero(5000)
        temp = self.value.get_extra()
        self.assertEqual(
            temp,
            ['$1000', '$1000', '$1000', '$1000', '$1000']
        )

    def test_5_error_more_money(self):
        with self.assertRaises(Exception) as context:
            self.value.extraer_dinero(12000)
        self.assertTrue(
            'El cajero solo tiene : 10000 y usted quiere retirar : 12000'
            in str(context.exception)
        )

    def test_6_error_not_m100(self):
        with self.assertRaises(Exception) as context:
            self.value.extraer_dinero(5520)
        self.assertTrue(
            'El monto solicitado no es multiplo de 100'
            in str(context.exception)
        )


# 10 billetes de $1000, 20 billetes de $500.
class TestCajero2(unittest.TestCase):

    def setUp(self):
        self.value = CajeroAutomatico()
        self.value.agregar_dinero([
            Bill_1000(), Bill_1000(), Bill_1000(), Bill_1000(), Bill_1000(),
            Bill_1000(), Bill_1000(), Bill_1000(), Bill_1000(), Bill_1000(),
            Bill_500(), Bill_500(), Bill_500(), Bill_500(), Bill_500(),
            Bill_500(), Bill_500(), Bill_500(), Bill_500(), Bill_500(),
            Bill_500(), Bill_500(), Bill_500(), Bill_500(), Bill_500(),
            Bill_500(), Bill_500(), Bill_500(), Bill_500(), Bill_500()
        ])
        self.value.contar_dinero()

    def test_7_contar_dinero_parciales(self):
        temp = self.value.get_billetes_parciales()
        self.assertEqual(
            temp, [['$100', 0], ['$200', 0], ['$500', 10000], ['$1000', 10000]]
            )

    def test_8_contar_billetes(self):
        temp = self.value.get_cant_billetes()
        self.assertEqual(
            temp, [['$1000', 10], ['$500', 20], ['$200', 0], ['$100', 0]])

    def test_9_total_dinero(self):
        temp = self.value.get_total_dinero()
        self.assertEqual(temp, 20000)

    def test_10_extraer_5000(self):
        self.value.extraer_dinero(5000)
        temp = self.value.get_extra()
        self.assertEqual(
        temp,
        ['$1000', '$1000', '$1000', '$1000', '$1000']
        )

    def test_11_extraer_12000(self):
        self.value.extraer_dinero(12000)
        temp = self.value.get_extra()
        self.assertEqual(
        temp,
        ['$1000', '$1000', '$1000', '$1000', '$1000',
        '$1000', '$1000', '$1000', '$1000', '$1000',
        '$500', '$500', '$500', '$500']
        )

    def test_12_extraer_12100(self):
        with self.assertRaises(Exception) as context:
            self.value.extraer_dinero(12100)
        self.assertTrue(
            'No hay una combinacion de billetes posible'
            in str(context.exception)
        )

    def test_13_extraer_7000_10por(self):
        self.value.extraer_dinero_cambio(7000, 10)
        temp = self.value.get_extra()
        self.assertEqual(
            temp,
            ['$1000', '$1000', '$1000', '$1000', '$1000',
            '$1000', '$500', '$500']
        )


# 10 billetes de $1000, 20 billetes de $500, 15 billetes de $200.
class TestCajero3(unittest.TestCase):
    def setUp(self):
        self.value = CajeroAutomatico()
        self.value.agregar_dinero([
            Bill_1000(), Bill_1000(), Bill_1000(), Bill_1000(), Bill_1000(),
            Bill_1000(), Bill_1000(), Bill_1000(), Bill_1000(), Bill_1000(),
            Bill_500(), Bill_500(), Bill_500(), Bill_500(), Bill_500(),
            Bill_500(), Bill_500(), Bill_500(), Bill_500(), Bill_500(),
            Bill_500(), Bill_500(), Bill_500(), Bill_500(), Bill_500(),
            Bill_500(), Bill_500(), Bill_500(), Bill_500(), Bill_500(),
            Bill_200(), Bill_200(), Bill_200(), Bill_200(), Bill_200(),
            Bill_200(), Bill_200(), Bill_200(), Bill_200(), Bill_200(),
            Bill_200(), Bill_200(), Bill_200(), Bill_200(), Bill_200(),
        ])
        self.value.contar_dinero()        

    def test_14_contar_dinero_parciales(self):
        temp = self.value.get_billetes_parciales()
        self.assertEqual(
            temp, [['$100', 0], ['$200', 3000], ['$500', 10000], ['$1000', 10000]]
            )

    def test_15_contar_billetes(self):
        temp = self.value.get_cant_billetes()
        self.assertEqual(
            temp, [['$1000', 10], ['$500', 20], ['$200', 15], ['$100', 0]])

    def test_16_total_dinero(self):
        temp = self.value.get_total_dinero()
        self.assertEqual(temp, 23000)

    def test_17_extraer_5000(self):
        self.value.extraer_dinero(5000)
        temp = self.value.get_extra()
        self.assertEqual(
        temp,
        ['$1000', '$1000', '$1000', '$1000', '$1000']
        )

    def test_18_extraer_12000(self):
        self.value.extraer_dinero(12000)
        temp = self.value.get_extra()
        self.assertEqual(
        temp,
        ['$1000', '$1000', '$1000', '$1000', '$1000',
        '$1000', '$1000', '$1000', '$1000', '$1000',
        '$500', '$500', '$500', '$500']
        )

    def test_19_extraer_12100(self):
        with self.assertRaises(Exception) as context:
            self.value.extraer_dinero(12100)
        self.assertTrue(
            'No hay una combinacion de billetes posible'
            in str(context.exception)
        )

    def test_20_extraer_7000_10por(self):
        self.value.extraer_dinero_cambio(7000, 10)
        temp = self.value.get_extra()
        self.assertEqual(
            temp,
            ['$1000', '$1000', '$1000', '$1000', '$1000',
            '$1000', '$200', '$200', '$200', '$200', '$200']
        )


if __name__ == "__main__":
    unittest.main()
