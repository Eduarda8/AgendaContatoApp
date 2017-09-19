
import json

    # Importação da biblioteca que formata a data de nscimento do usuario;
import datetime

    # Classe do Objeto Pessoa da agenda telefonica;
class Pessoa():

    # Função que vai receber os paramêtros informados no exercicío;
    def __init__(self,nome,nascimento,email):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email

    # Função __str__ (método mágico) do Objeto Pessoa;
    def __str__(self):
        return ("Nome: %s\n Nascimento: %s\n E-mail: %s"%(self.nome,str(self.nascimento),self.email))
