import abc


class Operacao(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

if __name__ == '__main__':
    main()