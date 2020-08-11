class Filme:
  def __init__(self, nome, ano, duracao):
    self.__nome = nome
    self.ano = ano
    self.duracao = duracao
    self.__likes = 0

  @property
  def likes(self):
    return self.__likes
    
  def dar_like(self):
    self.likes += 1

class Serie:
  def __init__(self, nome, ano, temporadas):
    self.nome = nome
    self.ano = ano
    self.teporadas = temporadas
    self.likes = 0

  def dar_like(self):
    self.likes += 1