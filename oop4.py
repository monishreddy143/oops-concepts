#memory aver loding in polymorphism concept
class student1:

	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3

	def  sum(self,a=None ,b=None,c=None):
		s=0
		if a!=None and b!=None and c!=None :
			 s=a+b+c	
		elif a!=None and b!=None :
			s=a+b
		else:
			s=a

		return s 


a=student1(33,88,66)

print(a.m1,a.m2,a.m3)
print(a.sum(22,44,55))
