'''
A lambda function is a small anonymous function and can take any number of arguments, but can only have one expression.
'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))