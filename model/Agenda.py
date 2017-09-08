#Importação da Classes que são necessarias para criar a Agenda.
from model.Pessoa import Pessoa
from model.Contato import Contato

    #leitor de arquivos em formato de dicionário;
import json

    #Criação da Agenda e suas funções;
class Agenda(Pessoa):

    def __init__(self,proprietario,contatos = []):
        self.proprietario = proprietario
        self.contatos = []

    def __str__(self):
        return "Proprietário: \n" + str(self.proprietario)

    # Conta o número de contatos existentes na Agenda;
    def contarContatos(self):
        return len(self.contatos)

    # Criação da lista de todos os contatos existentes na Agenda;
    def listarContatos(self):
        for contato in self.contatos:
            self.SalvarContato(contato)
        print()

    # Função para incluir um ou mais contatos em uma lista;
    def incluirContato(self, contato):
        self.contatos.append(contato)

    # Função para excluir um contato da lista, usando a função remove;
    def excluirContato(self, nome):
        self.contatos.remove(self.buscarContato(nome))

    # Função para buscar os contatdos adicionados na Agenda;
    def buscarConato(self, nome):
        for contato in self.contatos:
            if (contato['pessoa']['nome'].lower() == nome.lower()):
                return contato
        return None

    def salvarJson(self, contato):
        cont = open('Agenda.json', 'w')
        cont.write(contato)
