class Contato():
 
 	def __init__(self, criacao, nome,nascimento,email,numero,ddd,codigoPais):
   
 		self.criacao = criacao
   
 		self.nome = nome
    
		self.nascimento = nascimento
  
  		self.email = email
   
 		self.numero = numero
    
		self.ddd = ddd
    
		self.codigoPais = codigoPais
    
  

 	def __str__(self):
   
 		return "Contato: %s nascimento: %s email: %s numero: %s ddd: %s codigo Pais: %s"%(self.nome,self.nascimento,self.email,self.numero,self.ddd,self.codigoPais)
    
    
 
 	def listarTelefones(self):
   
 		return []