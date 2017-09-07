class Pessoa():
  
	def __init__(self, nome, nascimento, email):
    
		self.nome = nome
    self.nascimento = nascimento
    
		self.email = email
    
  
	def __str__(self):
    
		return "Proprietario: %s Nascimento: %s email: %s "%(self.nome,self.nascimento,self.email)