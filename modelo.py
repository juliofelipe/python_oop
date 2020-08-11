class Programa:
   def __init__(self, nome, ano):
    self.__nome = nome.title
    self.ano = ano
    self.__likes = 0

    @property
    def likes(self):
      return self.__likes

    def dar_like(self):
      self.likes += 1

    @property
    def nome(self):
      return self.__nome

    @nome.setter
    def nome(self, novo_nome):
      self.__nome = novo_nome.title()


class Filme:
    def __init__(self, nome, ano):
      self.__nome = nome.title
      self.ano = ano
      self.__likes = 0

class Serie:
  def __init__(self, nome, ano, temporadas):
    self.nome = nome
    self.ano = ano
    self.teporadas = temporadas
    self.likes = 0

  def dar_like(self):
    self.likes += 1