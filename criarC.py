from adimin import *

pessoa = []

def criar():
  while True:
    pessoa.append(Cardapio())
    pessoa[len(pessoa)-1] = FazerC()
    i = input("\ndeseja Cadastrar mais um?(s/n): ")
    if (i == "n" or i == "N"):
      return pessoa
      break

def criaropcao(q):
  pessoa = [Cardapio()] * q
  for i in range(q):
    pessoa[i] = opcao(i)
  return pessoa
