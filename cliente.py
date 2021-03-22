

from adimin import *
import os
from datetime import datetime
now = datetime.now()


def PrintPedidos(listape):
 
  os.system('clear') or None

  print("\n ######## PEDIDOS ######## \n")
  attPeso(listape,mini)
  for l in range(len(listape)):
    print("Mesa: " , listape[l][0] , " | prato: " , listape[l][1] , " | peso: " , listape[l][2] , " | tempo " , listape[l][3])

  print("\n ######## PEDIDOS ######## \n")

def pedidos(cardapio, listape):
  while True:
    os.system('clear') or None
    for i in range(len(cardapio)):
      print(i+1 , " = ", end="")
      Print(cardapio[i])
    x = input("\nDeseja fazer pedido(s/n): ")
    if(x == "n" or x == "N"):
      break
    i = int(input("\nQual prato: "))
    while i<=0 or i>=9:
      print("Valor invalido")
      x=int(input("Digite outro prato"))
    mesa = input("\nDe qual mesa: ")
    listape.append("")
    listape[len(listape)-1] = mesa, cardapio[i-1].nome, cardapio[i-1].peso, cardapio[i-1].tempo

vet = []
pelista = []
vmesa = []
vnome = []
vpeso = []
vtempo = []
mini=[]

def organiza(listape):
  
  for i in range(len(listape)):
    x = int(listape[i][2])
    vet.append(x)
  if len(vmesa) < len(listape):
    for j in range(len(listape)-len(vmesa)):
      vmesa.append("")
      vnome.append("")
      vpeso.append("")
      vtempo.append("")
      mini.append(now.minute)
  pelista = sorted(vet)
  pelista.reverse()
  for i in range(len(listape)):
    for j in range(len(listape)):
      c = int(pelista[i])
      v = int(listape[j][2])
      if (c == v):
        a = listape[j][0]
        b = listape[j][1]
        c = listape[j][2]
        d = listape[j][3] 
        listape[j] = listape[j][0],listape[j][1], 0 ,listape[j][3]
        vmesa[i] = "" + str(a)
        vnome[i] = "" + str(b)
        vpeso[i] = "" + str(c)
        vtempo[i] = "" + str(d)
        print(vmesa)
        print(listape)
        break
  for i in range(len(listape)):
    listape[i] = "" + str(vmesa[i]), "" + str(vnome[i]), "" + str(vpeso[i]), "" + str(vtempo[i])
  PrintPedidos(listape)
  for i in range(len(pelista)):
    pelista.pop()
    vet.pop()
    vmesa.pop()
    vnome.pop()
    vpeso.pop()
    vtempo.pop()
  attPeso(listape,mini)
  return listape


def exclui(listape):
  for l in range(len(listape)):
      print(l+1 , " = ", end="")
      print("Mesa: " , listape[l][0] , " | prato: " , listape[l][1] , " | peso: " , listape[l][2] , " | tempo " , listape[l][3])
  x = int(input("Qual deseja excluir da lista: "))
  del(listape[x-1])
  PrintPedidos(listape)

def attPeso(listape,mini):
  now2 = datetime.now()
  agr=now2.minute 
  x=[]
  for i in range(len(listape)):
    x.append(int(listape[i][2]))
  for i in range(len(mini)):
    if mini[i]==58 or mini[i]==59:
      mini[i]=0

  for i in range(len(listape)):
    for j in range(len(listape)):
      v = int(listape[j][2])
      if agr-mini[j]>=0 and agr-mini[j]<=2 :
        v+=2
        listape[j] = listape[j][0],listape[j][1], v ,listape[j][3]
        
      elif agr-mini[j]>=3 and agr-mini[j]<=4:
        v+=3
        listape[j] = listape[j][0],listape[j][1], v ,listape[j][3]
      elif agr-mini[j]>=4:
        v+=4
        listape[j] = listape[j][0],listape[j][1], v ,listape[j][3]
      v=0
    break

