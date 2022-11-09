class VendedorComissao:
    def __init__(self, codigo, nome, vendas, taxas):
        self._codigo = codigo
        self._nome = nome
        self._vendas = vendas
        self._taxas = taxas

    def calcularSalario():
        return vendas * taxas

    @property
    def codigo(self, codigo):
        return self._codigo

    @property
    def nome(self, nome):
        return self._nome

    @property
    def vendas(self, nome):
        return self._vendas

    @property
    def taxas(self):
        return self._taxas

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @vendas.setter
    def vendas(self, nome):
        self._vendas = vendas

    @taxas.setter
    def taxas(self):
        return self._taxas
