pi = 3.1214

def add(a,b):
       return a+b
def sub(a,b):
        return a - b 
def mul(a,b):
        return a * b 
def div(a,b):
        return a / b

a= int(input("Enter first number"))
b= int(input("Enter second number"))

#obj = cal(a,b)


while choice!=0:
	print("0. Exit")
	print("1. Add")
	print("2. Sub")
	print("3. Mul")
	print("4. Div")
	choice=int(input("Enter you choice"))	
	if choice==1:
		print(a,"+",b,"=",add(a,b))
	elif choice==2:
		print(a,"-",b,"=",sub(a,b))
	elif choice==3:
		print(a,"*",b,"=",mul(a,b))
	elif choice==4:
		print(a,"/",b,"=",div(a,b))
	elif choice==0:
		print("Exit")
	else:
		print("invalide choice");
