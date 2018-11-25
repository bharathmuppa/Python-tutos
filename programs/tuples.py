'''
A tuple is created by placing all the items (elements) inside a parentheses (), separated by comma. The parentheses are optional but is a good practice to write it.

A tuple can have any number of items and they may be of different types (integer, float, list, string etc.).
Creating a tuple with one element is a bit tricky.

Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is in fact a tuple.

'''

emptyTuple = ()
print(emptyTuple)
tupleWithMultipleDataTypes = (1,2,3,'a','b','c','asdad',[1,2,3],{'name':'bharat','phno':'687509074'},('a','b','c'))
print(tupleWithMultipleDataTypes)
oneArgasNumber = (1)
print(oneArgasNumber)
oneArgasTuple = 1,
print(oneArgasTuple)

'''
operations on tuples
'''
#my_tuple = ('a','p','p','l','e',)
#print(my_tuple.count('p'))
#print(my_tuple.index('l'))
#print(my_tuple[0:4])
#print('a' in my_tuple)
#print('g' not in my_tuple)

'''
iterations using tuples
'''
#for name in ('bharath','gowtham'):
#     print("Hello",name)  

'''
other operations
all() - Return True if all elements of the tuple are true (or if the tuple is empty).
any() - Return True if any element of the tuple is true. If the tuple is empty, return False.
enumerate() - Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
len() - Return the length (the number of items) in the tuple.
max()	Return the largest item in the tuple.
min()	Return the smallest item in the tuple
sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
sum()	Retrun the sum of all elements in the tuple.
tuple()	Convert an iterable (list, string, set, dictionary) to a tuple.
'''

someOtherDataType = {'name':'bharath'}
print(tuple(someOtherDataType))
# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1=',t1)

# one false value
#l = [1, 3, 4, 0]
#print(all(l))