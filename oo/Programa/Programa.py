class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @staticmethod
    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada

    @property
    def temporada(self):
        return self._temporada


##TESTE CLASSES
filme1 = Filme("homem aranha 3", 2012, 160)
mostrar_filme = (
    "Filme: {} \nLançamento: {} \nDuração: {} \nGostei: {}\n".format(filme1.nome, filme1.ano, filme1.duracao,
                                                                     filme1.likes))
serie1 = Serie("Brooklin 99", 2020, 8)
mostrar_serie = (
    "Série: {} \nLançamento: {} \nTemporadas: {} \nGostei: {}\n".format(serie1.nome, serie1.ano, serie1.temporada,
                                                                        serie1.likes))
print(mostrar_filme)
print(mostrar_serie)

filmes_e_series = [filme1, serie1]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada
    print(f'{programa.nome} - {detalhes} - {programa.likes}')
