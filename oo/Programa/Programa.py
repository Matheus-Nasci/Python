class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

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

    def __str__(self):
        return f"{self._nome} - {self._ano} - {self._likes} - Likes"


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    def __str__(self):
        return f"{self._nome} - {self._ano} - {self._duracao} Min - {self._likes} - Likes"


class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self._temporada = temporada

    @property
    def temporada(self):
        return self._temporada

    def __str__(self):
        return f"{self._nome} - {self._ano} - {self._temporada} temporadas - {self._likes} - Likes"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


##TESTE CLASSES
filme1 = Filme("homem aranha 3", 2012, 80)
filme2 = Filme("sherek", 2001, 100)
filme1.dar_like()
filme2.dar_like()
filme2.dar_like()

serie1 = Serie("Brooklin 99", 2020, 8)
serie2 = Serie("Demolidor", 2016, 2)
serie2.dar_like()
serie2.dar_like()
serie1.dar_like()
serie1.dar_like()

filmes_e_series = [filme1, serie1, serie2, filme2]
playlist_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

print(f"Tamanho Playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)

