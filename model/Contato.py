
    # Classe do Objeto contato da agenda telefonica;
class Contato():

    # (Precisa comentar)
    def __init__(self, criacao, pessoa):
        self.criacao = criacao
        self.pessoa = pessoa

    # (Precisa comentar)
    def listarTelefones(self):
        return self.telefones

    # (Precisa comentar)
    def __str__(self):
        return "Agenda[%s]"%(self.proprietario)
