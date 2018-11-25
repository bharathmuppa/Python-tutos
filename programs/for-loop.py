'''
range(start,stop,step size)
'''

print(list(range(2, 20, 3)))

# Program to iterate through a list using indexing

genre = ['carnatic', 'hindhusthani', 'baithak gana','jazz','blue','rock','metal']

# iterate over the list using index
for i in range(len(genre)):
    if i==2:
	    print("I don't like",genre[i])
    else:
        print("I liike", genre[i])