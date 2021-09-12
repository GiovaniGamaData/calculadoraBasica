from operacao import Operacao

class Divisao(Operacao):
    def executar (self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado


if __name__ == '__main__':
    main()