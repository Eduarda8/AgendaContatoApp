'''
Criação da Classe do objeto Telefone e adicionando
os seus atributos do telefone para cada contato;
'''

class Telefone():

    # Função que vai receber os paramêtros informados no exercicío;
    def __init__(self, numero, ddd, codigoPais):
        self.numero = numero
        self.ddd = ddd
        self.codigoPais = codigoPais

     # self.telefone = ("(" + str(self.numero) + " " + str(self.ddd) + ") " + str(self.codigoPais))

    # Método mágico __str__ do telefone;
    def __str__(self):
        return ("(" + str(self.numero) + " " + str(self.ddd) + ") " + str(self.codigoPais))
