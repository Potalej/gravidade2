from config.configs import animacao, dados
from auxiliares.auxiliares import momento_inercia_cm, centro_massas, complexidade
from auxiliares.hamiltoniano import H, U
from integracao.integracao import RK4 as metodo_integracao

from time import time
from numpy import true_divide

class Simulacao:
  """
    Para fazer simulações.
  """
  QUANTIDADE_ANTES_SALVAR = animacao['QUANTIDADE_ANTES_SALVAR']

  def __init__ (self, massas:list, R0: list, P0: list, h:float=0.05, G:float=1):
    self.massas = massas
    self.quantidade_corpos = len(self.massas)
    self.dimensao = len(R0[0])
    self.mtot = sum(self.massas)

    self.R, self.P = R0, P0

    # inicializa o método
    self.h = h
    self.metodo = metodo_integracao(self.massas, self.h, G=G, dimensao=self.dimensao)

    # energia inicial
    self.E0 = H(self.R, self.P, self.massas)
    self.E = self.E0

    # quantidade de integrações por passo
    self.n = 100

  def salvarPontos (self, pontos:list, nome='pontos.txt'):
    coords = [[str(ponto) for ponto in lista] for lista in pontos]
    coords = '\n'.join([','.join(ponto) for ponto in coords])
    with open('pontos/' + nome, 'a') as arq:
      arq.write('\n' + coords)

  def abrirArquivo (self, massas:list, nome='pontos.txt'):
    with open('pontos/' + nome, 'w') as arq:
      m = ','.join(str(m) for m in massas)
      arq.write(m + dados['SEPARADOR'][:-1])
