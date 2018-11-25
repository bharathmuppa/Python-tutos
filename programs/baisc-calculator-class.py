class cal():
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self):
		return self.a + self.b
	def sub(self):
		return self.a - self.b
	def mul(self):
		return self.a * self.b
	def div(self):
		return self.a / self.b

a= int(input("Enter first number"));
b= int(input("Enter second number"));
obj = cal(a,b)

choice =1 
while choice!=0:
	print("0. Exit")
	print("1. Add")
	print("2. Sub")
	print("3. Mul")
	print("4. Div")
	choice=int(input("Enter you choice"))	
	if choice==1:
		print(a,"+",b,"=",obj.add())
	elif choice==2:
		print(a,"-",b,"=",obj.sub())
	elif choice==3:
		print(a,"*",b,"=",obj.mul())
	elif choice==4:
		print(a,"/",b,"=",obj.div())
	elif choice==0:
		print("Exit")
	else:
		print("invalide choice");

