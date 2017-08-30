from model.Pessoa import Pessoa
import pickle
from model.Contato import Contato
class Agenda(Pessoa):

    def __init__(self,proprietario,nascimento,email):
        self.proprietario = proprietario
        self.nascimento = nascimento
        self.email = email


    def contarContatos(self):
        pass
    def listarContatos(self):
        pass


    def incluirContato(self):

        while ( x == 's'):

            c1 = Contato(criacao = input("Digite a data de hoje:\n"), nome = input("Nome do contato: \n"),email = input("Email:\n"), numero = input("Numero do telefone:\n"), ddd = input("ddd\n"), codigoPais = input("Codigo do Pais:\n"))           dicc = {'DATA DE CRIACAO DO CONTATO': c1.criacao, 'NOME': c1.nome, 'EMAIL': c1.email, 'NUMERO': c1.numero,'DDD': c1.ddd, 'CODIGO DO PAIS': c1.codigoPais }
            arquivo = open("contatos.json", 'wb')
            pickle.dump(dicc, arquivo)
            arquivo.close()
            arquivo = open("contatos.json", "rb")
            dicc = pickle.load(arquivo)
            arquivo.close()
            x = int(input("Deseja adicionar mais um contato ? \n"))

    def buscarConato(self):
          pass

    def excluirContato(self,nome):
        pass