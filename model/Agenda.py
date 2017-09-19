
    # Importação da Classes que são necessarias para criar a Agenda.
from model.Pessoa import Pessoa

    # leitor de arquivos em formato de dicionário;
import json

    #Criação da Agenda e suas funções;
class Agenda(Pessoa):

    def __init__(self,proprietario,contatos = []):
        self.proprietario = proprietario
        self.contatos = contatos

    def __str__(self):
        return "Agenda[proprietario: %s, contatos: %s]"%(self.proprietario, self.contatos)

    # Conta o número de contatos existentes na Agenda;
    def contarContatos(self):
        return len(self.contatos)

    # Criação da lista de todos os contatos existentes na Agenda;
    def listarContatos(self):
        for contato in self.contatos:
            print(contato)

    # Função para incluir um ou mais contatos em uma lista;
    def incluirContato(self, contato):
        self.contatos.append(contato)

    # Função para excluir um contato da lista, usando a função remove;
    def excluirContato(self, nome):
        for contato in self.contatos:
            if (contato.pessoa.nome.lower() == nome.lower()):
                self.contatos.remove(contato)
        return None

    # Função para buscar os contatdos adicionados na Agenda;
    def buscarContato(self, nome):
        for contato in self.contatos:
            if (contato.pessoa.nome.lower() == nome.lower()):
                return contato
        return None

    def salvarJson(self, contato):
        cont = open('Agenda.json', 'w')
        cont.write(contato)
