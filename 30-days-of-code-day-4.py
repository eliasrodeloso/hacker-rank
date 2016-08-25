class Person:
  
  def __init__(self,initialAge):
  	if not initialAge > 30 and initialAge >= -5:
  		if initialAge < 0:
	  		print('Age is not valid, setting age to 0.')
	  		self.age = 0
	  	else:
	  		self.age = initialAge

  def amIOld(self):
  	if self.age < 13:
  		print('You are young.')
  	elif self.age >= 13 and self.age < 18:
  		print('You are teenager.')
  	else:
  		print('You are old.')
      
  def yearPasses(self):
  	self.age = self.age + 1
