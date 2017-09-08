import json

    # Importação da biblioteca que formata a data de nscimento do usuario;
import datetime

    # Classe do Objeto Pessoa da agenda telefonica;
class Pessoa():

    # Função que vai receber os paramêtros informados no exercicío;
    def __init__(self,nome,nascimento,email):
        self.nome = str(input("Infome o seu nome:"))
        self.nascimento = datetime.date()
        self.email = str(input("Infome o seu email:"))

    # Função __str__ (método mágico) do Objeto Pessoa;
	def __str__(self):
		return "Proprietario: %s Nascimento: %s email: %s "%(self.nome,self.nascimento,self.email)
