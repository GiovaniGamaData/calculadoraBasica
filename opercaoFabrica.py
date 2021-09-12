from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao


class OperacaoFabrica(object):
    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif(operador == 'subtracao'):
            return Subtracao()
        elif(operador == 'multiplicacao'):
            return Multiplicacao()
        elif(operador == 'divisao'):
            return Divisao()


if __name__ == '__main__':
    main()