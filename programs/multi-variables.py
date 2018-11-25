def lessThan(cutoffVal, *vals) :
    ''' Return a list of values less than the cutoff. '''
    arr = []
    for val in vals :
        if val < cutoffVal:
            arr.append(val)
    return arr
print(lessThan(10, 2, 17, -3, 42))