print('''
print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)
''')
print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&

print('I love {0} and {1}'.format('bread','butter'))
#print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

x=23.123123123
print('The value of x is %3.4f' %x)

#python old version
name = "Bharath"
age = 16
print("Hello, %s. You are %s." % (name, age))

#python 2.6
print("Hello, {1}. You are {0}.".format(age, name))
person = {'name': 'bharath', 'age': 28}

print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))
print("Hello, {name}. You are {age}.".format(**person))

#python 3.3 and above
print(f"Hello, {name}. You are {age}.")

# As f' or F" executed at run time we can use 
def to_lowercase(input):
    return input.lower()

print(f"{to_lowercase(name)} is funny.")


