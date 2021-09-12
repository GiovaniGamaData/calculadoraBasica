from unittest import TestCase, main
from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao
from calculadora import Calculadora

class Teste():
    def soma_test(self):
        calculador = Calculadora()
        self.assertEqual(calculador.calcular(2,3, 'soma'),resultado, 5)

    def subtracao_test(self):
        calculador2 = Calculadora()
        self.assertEqual(calculador2.calcular(3,2, 'subtracao'),resultado, 1)

    def subtracao_test(self):
        calculador3 = Calculadora()
        self.assertEqual(calculador3.calcular(4,2, 'divisao'),resultado, 2)

    def subtracao_test(self):
        calculador4 = Calculadora()
        self.assertEqual(calculador4.calcular(3,2, 'multiplicacao'),resultado, 6)

if __name__ == '__main__':
    main()