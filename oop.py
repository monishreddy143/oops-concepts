class student:#outer class
	
	def __init__(self,name,rolnum):
		self.name=name
		self.rolnum=rolnum
		self.lap=self.laptop()

	def show(self):
		print(self.name,self.rolnum)
		self.lap.show()
#inner class
	class laptop:
		def __init__(self):
			self.brand='hp'
			self.ram=8
			self.cpu='i3'


		def show(self):
			print(self.brand,self.cpu)

		def star(self):
			a=[1,2,3,4]
			for i in a:
				print(i*'*')



s1=student('monish',33)
s1.lap.star()
print(s1.show())
