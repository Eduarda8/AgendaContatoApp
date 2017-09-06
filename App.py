from model.Contato import Contato
from model.Pessoa import Pessoa
from model.Agenda import Agenda
from model.Telefone import Telefone
from datetime import datetime


def main():
        #Criação da função menu para a agenda telefônica;
        #criarPessoa()

    def criarPessoa():
        nome = input("Informe o nome do proprietário:")
        nascimento = input("Informe a data do nascimento do proprietário:")
        email = input("Informe o email do proprietário:")
        pessoa = Pessoa(nome, nascimento, email)

        return pessoa

    def criarContato():

        # Adicionando os dados do Propietário
        pessoa = criarPessoa()
        criacao = input("Criação do contato:")
        contato = Contato(pessoa)

    def criarAgenda():
        #cadastro do proprietário
        nome = input("Informe o nome do proprietário:")
        nascimento = input("Informe a data do nascimento do proprietário:")
        email = input("Informe o email do proprietário:")

        proprietario = Pessoa(nome,nascimento,email)
        agenda = Agenda(proprietario)

        # Criação da função menu para a agenda telefônica;
        def menu():
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
                    pass
            except:
                print("Infelizmente ouve um erro... Please, tente novamente !")

if __name__ == "__main__":
    main()