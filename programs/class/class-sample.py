'''
A class creates a new local namespace where all its attributes are defined. Attributes may be data or functions.
'''

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)

# call: call func function
a.func()

'''
You may have noticed the self parameter in function definition inside the class but,
we called the method simply as ob.func() without any arguments. It still worked.
This is because, whenever an object calls its method, the object itself is passed as the first argument. 
So, ob.func() translates into MyClass.func(ob).
'''