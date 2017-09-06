
    #Importação da Classes que são necessarias para criar a Agenda.
from model.Pessoa import Pessoa
from model.Contato import Contato

    #Criação da Agenda e suas funções
class Agenda(Pessoa):

    # (Precisa comentar)
    def __init__(self,proprietario,contatos = []):
        self.proprietario = proprietario
        self.contatos = []

    # (Precisa comentar)
    def __str__(self):
        return "Agenda[%s]"%(self.proprietario)

    # (Precisa comentar)
    def contarContatos(self):
        contato = Contato()
        return len(self.contatos)

    # (Precisa comentar)
    def listarContatos(self):
        return self.contatos

    # Função para incluir um ou mais contatos em uma lista;
    def incluirContato(self, contato):
        self.contatos.append(contato)
        print("Contato adicionado na Agenda")

    # Função para excluir um contato da lista;
    def excluirContato(self, nome):
        nome = input("Qual contato você dejesa excluir:")
        Agenda.excluirContato(nome)

    # Função para buscar os contatdos adicionados na Agenda;
    def buscarConato(self):
          pass