from adimin import *
from cliente import *
from criarC import *
import os


# FUNCIONÁRIO

def menu1():
  print("\n----------INICIALIZAÇÃO DO SISTEMA----------\n") 
  print("- 1 --> FAZER CARDAPIO             -")
  print("- 2 --> USAR CARDAPIO SISTEMA      -")
  i = int(input("\nQual opcao deseja:   "))
  return i

def menu2():
  print("\n-----------CONFIGURAÇÃO DO SISTEMA----------\n")
  print("- 1 --> ADICIONAR PEDIDO CARDAPIO  -")
  print("- 2 --> RETIRAR PEDIDO CARDAPIO    -")
  print("- 3 --> PRINTAR CARDAPIO           -")
  print("- 4 --> INICIAR JORNADA            -")
  i = int(input("\nQual opcao deseja:   "))
  return i


i = menu1()
while True:
  os.system('clear') or None
  if i == 1 :
    cardapio = criar()
    break
  elif i == 2:
    cardapio = criaropcao(10)
    break
  else:
    print("por favor digite 1 ou 2! ")
  i = menu1()

i = menu2()
while True: 
  os.system('clear') or None
  if i == 1:
    cardapio = AddCardapio(cardapio)
  elif i == 2:
    cardapio = ReCardapio(cardapio)
  elif i == 3:
    for i in range(len(cardapio)):
      Print(cardapio[i])
  elif i == 4:
    break
  else:
    print("por favor digite um numero correspondente ao pedido no menu")
  i = menu2()


  #CLIENTE 


def menu():
  print("\n----------CLIENTE----------\n") 
  print("- 1 --> CADASTRAR PEDIDO       -")
  print("- 2 --> EXCLUIR PEDIDO         -")
  print("- 3 --> LISTAR PEDIDOS         -")
  print("- 4 --> PEGAR PEDIDO           -")
  print("- 5 --> ENCERRAR               -")
  i = int(input("\nQual opcao deseja:   "))
  while i<0 or i>5: 
    i=int(input("Por favor digite um numero correspondente ao pedido no menu"))
  return i

listape = []

i = menu()
while True: 
  os.system('clear') or None
  if i == 1:
    pedidos(cardapio, listape)
    listape = organiza(listape)
  elif i == 2:
    exclui(listape)
    listape = organiza(listape)
  elif i == 3:
    PrintPedidos(listape)
  elif i == 4:
    if(len(listape)>0):
      del(listape[0])
  else:
    break
  
  i = menu()

