class Programa:
   def __init__(self, nome, ano):
    self._nome = nome.title
    self.ano = ano
    self._likes = 0

    @property
    def likes(self):
      return self._likes

    def dar_like(self):
      self.likes += 1

    @property
    def nome(self):
      return self._nome

    @nome.setter
    def nome(self, novo_nome):
      self.__nome = novo_nome.title()


class Filme:
    def __init__(self, nome, ano, duracao):
      super().__init__(nome, ano)
      self.duracao = duracao
      self.__likes = 0

    def __str__(self):
      return f'{self._nome} - {self.ano}'

class Serie:
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome, ano)
    self.teporadas = temporadas
    self.likes = 0

  def dar_like(self):
    self.likes += 1

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


vigadores = Filme('vingadores - guerra infinita', 2018, 160)


for programa in playlist_fim_de_semana:
  print(programa)