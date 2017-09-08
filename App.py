import json
import datetime
from model.Agenda import Agenda
from model.Pessoa import Pessoa
from model.Telefone import Telefone
from model.Contato import Contato

# Criação da função menu para a agenda telefônica;
def para_dict(agenda):
    global obj, obj
    if hasattr(agenda, '__dict__'):
        agenda = agenda.__dict__
    if isinstance(agenda, dict):
        return {k: para_dict(v) for k, v in agenda.items()}
    elif isinstance(agenda, list) or isinstance(agenda, tuple):
        return [para_dict(e) for e in agenda]
    else:
        return agenda

def main():
       # criar Pessoa()
    def criarPessoa():
      
        nome = input("Informe o nome do proprietário:")
        nascimento = input("Informe a data do nascimento do proprietário:")
        email = input("Informe o email do proprietário:")
        pessoa = Pessoa(nome, nascimento, email)
        return pessoa
        
        x = open("Agenda.json","r", encoding='utf8')
        agendaJson = json.load(x)
        agenda = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        numero = input("Informe o numero do proprietário:")
        ddd = input("Informe o ddd so proprietário:")
        codigoPais = input("Informe o código do país do proprietário:")

        telefone = Telefone(numero, ddd, codigoPais)
        contato = Contato(pessoa, telefone)
        agenda.incluirContato(contato)
        return telefone

        aJson = json.dumps(para_dict(agenda))
        x = open("Agenda.json", "w", encoding='utf8')
        x.write(aJson)

    # Criação da função menu para a agenda telefônica;
    def menu():

        while True:
            print("===== Menu - Agenda Telefônica =====\n"

                    "1 - Incluir Contato \n"
                    "2 - Listar contatos \n"
                    "3 - Remover contato \n"
                    "4 - Buscar contato \n "
                    "5 - Quantidade de contatos \n"
                    "6 - Sair \n")

            # Tratando com as possiveis erros ou exceções que pode ocorrer na resposta do usuario;
            try:
                resp = input("Informe a opção desejada: ")
                if (resp == 1):
                    resp.incluirContato()
                elif (resp == 2):
                    resp.listarContatos()
                elif (resp == 3):
                    resp.excluirContato()
                elif (resp == 4):
                        resp.buscarContato()
                elif (resp == 5):
                    resp.contarContatos()
                elif (resp == 6):
                    print(" ~ Você saiu... thanks ~ ")

            except (ValueError, NameError):
                print("Infelizmente ouve um erro... Please, tente novamente !")
                break

if __name__ == '__main__':
    main()
