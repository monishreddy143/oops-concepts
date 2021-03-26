#inheritance
#super() method will allow the sub class ti acces any class constructers and 
#als0 it is use  to acces the methods also 
class grandpa:
	#constructers in inheritance
	def __init__(self):
		print("my son is father class")

	def name1(self):
		print("my name is monish im aged")

	def age1(self):
		print('my age is 70')

class father(grandpa):#[father:]

	def __init__(self):
		print("my son  is child class")
		super().__init__()
	

	def name2 (self):
		print('my name is roshan  im middle aged')

	def age2 (self):
		print('my age is 40')


	def show(self):
		print(sis.name1(),sis.name2())

class child(father,grandpa):#[chile(grandpa , father)]#multilevel inheritance

	def __init__(self):
		print('im the son of father class')
		super().__init__() 

	def name3(self):
		print('my nams is  munny im young')

	def age3(self):
		print("my age is 20")


	def show(self):
		print(sis.name1(),sis.name3())
		super().show()

#note-if there is no constructre in the sub class sthen the constructer in  super class will be used in subclasss

sis =child()
sis.show()