
'''
Criação da classe do Objeto Contato e
os seus atributos de um Contato;
'''

    # Importação das classes necessarias para a execução do Contato;
from model.Pessoa import Pessoa
from model.Telefone import Telefone
import datetime
import json

    # Criação de uma lista de Contatos;
relacaoContato = []

    # Classe do Objeto contato da agenda telefonica;
class Contato(Telefone):

    # (Precisa comentar)
    def __init__(self, criacao, pessoa):
        self.criacao = datetime.date.today() # Mostra a data do dia da execução do programa
        self.pessoa = Pessoa
        self.telCont = Telefone()
        self.contato = (str(self.criacao)+" "+ str(self.pessoa)+" "+ str(self.telCont))

        # Essa função (append), vai adicionar cada telefone em uma lista;
        relacaoContato.append(self.contato)

    # (Precisa comentar)
    def listarTelefones(self):
        return self.telefones

    # Método mágico __str__ do Contato;
    def __str__(self):
        return("Data da Criação: "+ str(self.criacao)+"\nContato: \n"+str(self.pessoa)+"\nNúmero: "+str(self.telCont))
