from opercaoFabrica import OperacaoFabrica
from operacao import Operacao

class Calculadora(object):
    def cacular(self, valor1, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

if __name__ == '__main__':
    main()