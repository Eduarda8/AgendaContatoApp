def menu():
  print("MENU\n")
  print("1- Incluir Contato\n")
  print("2- Listar Contatos\n")
  print("3- Remover Contatos\n")
  print("4- Buscar Contato\n")
  print("5- Quantidade de Contatos\n")
  print("6- Sair\n")

def criarProrietario():
  
  nome = str(input("Digite Seu Nome:\n"))
  nascimento = str(input("Digite Sua Data de Nascimento:\n"))
  email = str(input("Digite Seu Email:\n"))
  proprietario = Pessoa(nome, nascimento, email)
  return proprietario
  
def adicionar():
   
   nome = str(input("Digite Seu Nome:\n"))
   nascimento = str(input("Digite Sua Data de Nascimento:\n"))
   email = str(input("Digite Seu Email:\n"))
   numero = str(input("Digite o Numero do Contato:\n"))
   ddd = str(input("Digite o DDD:\n"))
   codigoPais = str(input("Digite o Código do Pais:\n"))
   criacao = str(input("Digite a Data de Criação:\n"))
   
   contato = Contato(nome, nascimento, email, numero,ddd,codigoPais,criacao)
   
   listadecontatos =[contato.nome, contato.nascimento ,contato.email,contato.numero ,contato.ddd, contato.codigoPais ,contato.criacao] 
   
   return listadecontatos
   
   
   
  
  

menu()

agenda = criarProrietario()



continuar = True
while continuar == True:
  try:
    op = int(input("Escolha uma Opção"))
    if (op == 1):
      ad = adicionar()
      print("Deseja Adicionar Outro Contato: s/n")
      resp = input()
      
      if (resp == "s"):
        
        while (resp == "s"):
          if (resp == "s"):
           
            ad = ad.append(adicionar())
            print("Deseja Adicionar Outro Contato: s/n")
            resp = input()
          else:
            continuar = False
      
    elif (op == 2):
      print(ad)
    elif (op == 3):
      pass
    elif (op == 4):
      pass
    elif (op == 5):
      pass
    else:
      continuar = False
      
  except (ValueError, NameError):
    print("Ops! Opção Inválida ")

