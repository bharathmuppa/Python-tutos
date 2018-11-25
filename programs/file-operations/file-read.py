'''
f = open("test.txt",mode = 'r',encoding = 'utf-8')
w  write mode
r  read mode
a  append mode

w+  create file if it doesn't exist and open it in write mode
r+  open an existing file in read+write mode
a+  create file if it doesn't exist and open it in append mode
'''

try:
   f = open("test.txt",'r',encoding = 'utf-8')
   f.read()
   f.tell()    # get the current file position
   f.seek(0)   # bring file cursor to initial position
   #for line in f:
   #	print(line, end = '')
   # perform file operations
finally:
   f.close()