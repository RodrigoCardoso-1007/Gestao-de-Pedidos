import os

class Cardapio():
  nome = ""
  tempo = 0
  peso = 0

def FazerC():
  Car = Cardapio()
  os.system('clear') or None
  print("\n------ CADASTRA ------\n")
  Car.nome = input("Nome do prato: ")
  Car.peso = int(input("Qual é o peso do prato: "))
  Car.tempo = int(input("Tempo medio de preparo: "))
  return Car

def opcao(i):
  pessoa = Cardapio()
  '''pessos =     
                t <= 5  == 10
          5  < t <= 10 ==  9
          10 < t <= 15 ==  8
          15 < t <= 20 ==  7
          20 < t <= 25 ==  6
          25 < t <= 30 ==  5
          30 < t <= 40 ==  4
          40 < t <= 50 ==  3
          50 < t <= 60 ==  2
               t >  60 ==  1
              
  '''
  if (i == 0):
    pessoa.nome = "batata frita"
    pessoa.peso = 10
    pessoa.tempo = 5
    return pessoa
  elif(i == 1 ):
    pessoa.nome = "hamburguer de siri"
    pessoa.peso = 7
    pessoa.tempo = 20
    return pessoa
  elif(i == 2 ):
    pessoa.nome = "macarrão na chapa"
    pessoa.peso = 5
    pessoa.tempo = 30
    return pessoa
  elif(i == 3 ):
    pessoa.nome = "bacalhau"
    pessoa.peso = 3
    pessoa.tempo = 50
    return pessoa
  elif(i == 4 ):
    pessoa.nome = "salada"
    pessoa.peso = 10
    pessoa.tempo = 5
    return pessoa
  elif(i == 5 ):
    pessoa.nome = "pastel de frango"
    pessoa.peso = 9
    pessoa.tempo = 10
    return pessoa
  elif(i == 6 ):
    pessoa.nome = "baião de dois"
    pessoa.peso = 4
    pessoa.tempo = 40
    return pessoa
  elif(i == 7 ):
    pessoa.nome = "cachorro quente"
    pessoa.peso = 7
    pessoa.tempo = 15
    return pessoa
  elif(i == 8 ):
    pessoa.nome = "rabada"
    pessoa.peso = 3
    pessoa.tempo = 45
    return pessoa
  elif(i == 9 ):
    pessoa.nome = "caudo de mocoto"
    pessoa.peso = 4
    pessoa.tempo = 40
    return pessoa
  
  
def Print(cardapio):
  print("prato :" , cardapio.nome , end = " ")
  print(" | peso :" , cardapio.peso , end = " ")
  print(" | tempo :" , cardapio.tempo)

def AddCardapio(cardapio):
  while True:
    os.system('clear') or None
    cardapio.append(Cardapio())
    cardapio[len(cardapio)-1] = FazerC()
    x = input("\ndeseja Cadastrar mais um?(s/n): ")       
    print("\n") 
    if (x == "n" or x == "N"):
      os.system('clear') or None
      for i in range(len(cardapio)):
        Print(cardapio[i])
      return cardapio
      break

def ReCardapio(cardapio):
  while True:
    os.system('clear') or None
    for i in range(len(cardapio)):
      print(i+1 , " = ", end="")
      Print(cardapio[i])
    y = int(input("\nQual prato deseja exluir: "))
    if (not y > len(cardapio)):
      del(cardapio[y-1])
    x = input("\ndeseja excluir mais um?(s/n): ")
    print("\n")    
    if (x == "n" or x == "N"):
      os.system('clear') or None
      for i in range(len(cardapio)):
        Print(cardapio[i])
      return cardapio
      break