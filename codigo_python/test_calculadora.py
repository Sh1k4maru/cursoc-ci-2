import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.cal = Calculadora()
        
    def test_sumar_2_mas_2(self):
       resultado = self.cal.sumar(2, 2)
       esperado = 4
       self.assertEqual(esperado, resultado)
      
    def test_sumar_5_mas_0(self):
        resultado = self.cal.sumar(5, 0)
        esperado = 5
        self.assertEqual(esperado, resultado)

    def test_sumar_menos_5_mas_3(self):
        resultado = self.cal.sumar(-5, 3)
        esperado = -2
        self.assertEqual(esperado, resultado)

    def test_sumar_5_punto3_mas_8(self):
        resultado = self.cal.sumar(5.3, 8)
        esperado = 13.3
        self.assertEqual(esperado, resultado)


if __name__ == '__main__':
    unittest.main()