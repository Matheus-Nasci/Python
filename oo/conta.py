class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um Objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifaTransferencia = 8.0

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.saldo += valor

    def __pode_sacar(self, valor_saque):
        return valor_saque <= self.__saldo

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("Seu saldo é R$: {}, o valor do saque passou do limite".format(round(self.__saldo, 2)))

    def transferir(self, valor, destino):

        valorTotal = valor + self.__tarifaTransferencia
        if valorTotal < (self.__saldo + self.__limite):

            self.__saldo -= valorTotal
            destino.deposita(valor)

            print("Transferência efetuada.")
        else:
            print("Saldo insuficiente.")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'Banco Brasil' : '001', 'Caixa' : '104', 'Bradesco' : '237', 'Safra' : '101'}

