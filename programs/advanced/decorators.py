print('''
@make_pretty
def ordinary():
    print("I am ordinary")

	is equivalent to below funciton

	def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)


so lets check below example which helps in reducing  risk of interpreted error


''')



def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

# divide(2,5)
# divide(2,0)


'''
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner
'''
