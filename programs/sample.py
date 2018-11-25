#%% [markdown]
# 
# # Programming is fun
# 
# ## introduction to python 
# 
# Before getting started, lets get familiarized with the language first.
# 
# Python is a general-purpose language. It has wide range of applications from Web development (like: Django and Bottle), scientific and mathematical computing (Orange, SymPy, NumPy) to desktop graphical user Interfaces (Pygame, Panda3D).
# 
# The syntax of the language is clean and length of the code is relatively short. It's fun to work in Python because it allows you to think about the problem rather than focusing on the syntax.
# 
# 
# ## History of Python
# 
# * Python is a fairly old language created by Guido Van Rossum. 
# * The design began in the late 1980s and was first released in February 1991. 
# 
# ## Why Python was created?
# 
# * In late 1980s, Guido Van Rossum was working on the Amoeba distributed operating system group.
# * He wanted to use an interpreted language like ABC (ABC has simple easy-to-understand syntax) 
# * that could access the Amoeba system calls. So, he decided to create a language that was extensible. 
# * This led to design of a new language which was later named Python.
# 
# ## Why the name Python?
# 
# * No. It wasn't named after a dangerous snake.
# * Rossum was fan of a comedy series from late seventies. 
# * The name "Python" was adopted from the same series "Monty Python's Flying Circus".
# 
# ## Features of Python Programming
# 
# ### A simple language which is easier to learn
# 
# * Python has a very simple and elegant syntax. It's much easier to read and write Python programs compared to other languages     like: C++, Java, C#.
# * Python makes programming fun and allows you to focus on the solution rather than syntax.
#     If you are a newbie, it's a great choice to start your journey with Python.
#     
# ### Free and open-source
# 
#   * You can freely use and distribute Python, even for commercial use. Not only can you use and distribute softwares written in     it, you can even make changes to the Python's source code. Python has a large community constantly improving it in each         iteration.
# 
# ### Portability
# 
#    * You can move Python programs from one platform to another, and run it without any changes.
#    * It runs seamlessly on almost all platforms including Windows, Mac OS X and Linux.
#     
# ### Extensible and Embeddable
# 
#   * Suppose an application requires high performance. You can easily combine pieces of C/C++ or other languages with Python    code.
#     This will give your application high performance as well as scripting capabilities which other languages may not provide out of the box.
#     
# ### A high-level, interpreted language
# 
#   * Unlike C/C++, you don't have to worry about daunting tasks like memory management, garbage collection and so on.
#     Likewise, when you run Python code, it automatically converts your code to the language your computer understands. You    don't need to worry about any lower-level operations.
# 
# ### Large standard libraries to solve common tasks
# 
#   * Python has a number of standard libraries which makes life of a programmer much easier since you don't have to write all the code yourself. For example: Need to connect MySQL database on a Web server? You can use MySQLdb library using import MySQLdb .
#   * Standard libraries in Python are well tested and used by hundreds of people. So you can be sure that it won't break your application.
#     
# ### Object-oriented
# 
#    * Everything in Python is an object. Object oriented programming (OOP) helps you solve a complex problem intuitively.
#    * With OOP, you are able to divide these complex problems into smaller sets by creating objects
#    
# ## Why Python ? 
# 
# ### Simple Elegant Syntax
#  * Programming in Python is fun. It's easier to understand and write Python code. Why? The syntax feels natural. Take this source code for an example:
#  ```python
# a = 2
# b = 3
# sum = a + b
# print(sum)
# ```
# 
# 
#%% [markdown]
# ### Not overly strict
# 
# * You don't need to define the type of a variable in Python. Also, it's not necessary to add semicolon at the end of the statement.
# * Python enforces you to follow good practices (like proper indentation). These small things can make learning much easier for beginners.
# 
# ### Expressiveness of the language
# 
# * Python allows you to write programs having greater functionality with fewer lines of code. Here's a link to the source code of   [Tic-tac-toe game](https://pastebin.com/7LTkj2V5) with a graphical interface and a smart computer opponent in less than 500 lines of code. This is just an example. You will be amazed how much you can do with Python once you learn the basics.
# 
# ### Great Community and Support
# 
#  * Python has a large supporting community. There are numerous active forums online which can be handy if you are stuck. 
#  
#  
# #### Coding Guide lines 
# * [Google coding guide line](https://google.github.io/styleguide/pyguide.html)
#  
#  # So Lets Jump into python coding
#  
#  
#  ## First Program

#%%
get_ipython().run_line_magic('write', 'hello_quantum.py')


#%%
# %load out-puts.py

'''
print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)
'''

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


