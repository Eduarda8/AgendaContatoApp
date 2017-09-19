
'''
Criação da classe do Objeto Contato e
os seus atributos de um Contato;
'''

    # Importação das classes necessarias para a execução do Contato;
from model.Pessoa import Pessoa
import datetime
import json

    # Classe do Objeto contato da agenda telefonica;
class Contato(Pessoa):

    # (Precisa comentar)
    def __init__(self, criacao, pessoa, telefone = []):

        self.criacao = criacao

    # self.criacao = datetime.date.today() # Mostra a data do dia da execução do programa

        self.pessoa = pessoa
        self.telCont = telefone
        self.contato = (str(self.criacao)+" "+ str(self.pessoa)+" "+ str(self.telCont))

    # (Precisa comentar)
    def listarTelefones(self):
        return self.telCont

    # Método mágico __str__ do Contato;
    def __str__(self):
        return ("Data da Criação: "+ str(self.criacao)+"\nContato: \n"+str(self.pessoa)+"\nNúmero: "+str(self.telCont))
