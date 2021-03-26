#operaters in  oop

class  student :

	def __init__ (self,m1,m2):
		self.m1=m1
		self.m2=m2

	def __add__(self,other):
		m1=self.m1 + other.m1
		m2=self.m2 + other.m2
		c=student(m1,m2) 
		return c

	def __mul__(self,other):
		m1=self.m1 * other.m1
		m2=self.m2 * other.m2
		c=student(m1,m2) 
		return c

	def __gt__(self,other):
		r1=self.m1 + other.m2
		r2=self.m1+other.m2
		if r1 > r2:
			return True
		else:
			return False

	def __str__(self):
		return    f'{self.m1} {self.m2} '


a=student(20,50)
b=student(30,66)

c= a*b
print(c.m1)

if a>b:
	print('a wins')
else:
	print('b wins')

d=10
print(d)
  #or 

print(d.__str__())#for th no need of method
 
print(a.__str__())#for this we need to define a method 
print(b.__str__())

