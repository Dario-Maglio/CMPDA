#Basic tutorial

a=int(input('Write an integer: '))
s=input('Write a string: ')
print(s+'\n'+s*a)
# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)


#data structures------------------------------------------------
   #list
print('\nLists')
lists=[3,5,[4,3],'Hi',7.4]
print(lists)
lists[1]=s[0]
print(lists+['a',2]) #addedd and multip like strings
B= (3 in lists) #true or false
lists.append(B)
print (lists)
lists.insert(0,len(lists))
print (lists)
print(lists.index(s[0]))
numbers = list(range(20, 5, -2))
#list slice
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[2:8:3])
print(squares[::-1])
#other way to defin lists
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

   #Dictionary
print('\nDictionary')
#a new dictionary key can also be assigned a value
squares = {1: 1, 2: [3,5,7], 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)
print(3 in squares)
#A useful dictionary method is get. It does the same
#thing as indexing, but if the key is not found in the
#dictionary it returns another specified value instead
#('None', by default)
pairs = {1: "apple",
  "orange": [2, 3, 4],
  True: False,
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

   #Tuples
print('\nTuples')#immutable list
words = ("spam", "eggs", "sausages",)
print(words[0]+'\n')

   #Sets
print('\nSets')
#Sets differ from lists in several ways, but share several list operations such as len.
#They are unordered, which means that they can't be indexed.
#They cannot contain duplicate elements.
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

first.add(23)
second.add(42)
print(first | second)#union
print(first & second)#intersection
print(first - second)#difference
print(second - first)
print(first ^ second)#symmetric difference

"""
When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.
"""

#control structures---------------------------------------------
input('Control structures')
print('\nIf')
if a == 5:
   print("Base is 5")
elif (a!= 11 and a!= 5):
   print("Base isn't 5 or 11")
else:
   print("Base is 11")
print('\n')

print('\nLoop')
i = 0
while B:
   i+=1
   if i == 2:
      print("Skipping 2")
      continue #jump to the next iteraction
   if i == 5:
      print("Breaking")
      break    #break the cycle
   print(i)
print("Finished")
print('\n')

for num in numbers:#each element in numbers
   print(num)
   print('\n')

#Type_of_Errors-------------------------------------------------
input('Errors')
"""
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type,
            but with an inappropriate value.
"""
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")
finally: #usefull to close file
   print("This code will run no matter what")

name = "123"
#raise NameError("Invalid name!")    raise give error
print(1)
assert 2 + 2 == 4
print(2)
#assert 1 + 1 == 3  -> assertionerror
print(3)


#functions------------------------------------------------------
input('\nFunctions and modules')

def maximum(x, y):
    if x >=y:
        return x
        print('This will not be printed')
    else:
        return y
        print('This will not be printed')

print(maximum(4, 7))
z = maximum(8, 5)
print(z)

def prod(x,y):
   return x*y

def twice(fun,x,y):
   return fun(fun(x,y),fun(x,y))

print(twice(prod,a,2))

   #other function
print('\nother function')
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums): #enumerate make a list with index
   print(v)

print(min([1, 2, 3, 4, 0, 2, 1]))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

   #pure functions
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#The function map takes a function and an iterable as arguments,
#and returns a new iterable with the function applied to each
#argument.
def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#The function filter filters an iterable by removing items that
#don't match a predicate (a function that returns a Boolean).
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#yeld make infinite lists as function
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))

   #recursion
def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(23))


#modules--------------------------------------------------------
import random

for i in range(5):
   value = random.randint(1, 6)
   print(value)

from math import pi
print(pi)

from math import sqrt as square_root
print(square_root(100))

from itertools import product, permutations
letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

random.__file__ """Trovare il percorso sul disco di una libreria"""

import math
dir(math) """Info su funzioni all'interno"""
help(math)

locals().keys() """lista tutti oggetti in uso,
                   locals() è un dizionario"""


"""Carrellata moduli std"""
[ random.gauss(0.,1.) for i in range (10)]


#files----------------------------------------------------------
input('Files')
"""
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.
Adding "b" to a mode opens it in binary mode,
which is used for non-text files (such as image and sound files).
"""
file = open("newfile.txt", "w")
# do stuff to the file
l=file.write("This has been written to a file\n")
file.write("This has been written to a file1\n")
file.write("This has been written to a file2\n")
file.write("This has been written to a file3\n")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()
file = open("newfile.txt", "r")
print(file.read(l)) #to print the first l byte of the file
print(file.readlines()) #make a list of the lines
file.close()
"""
When a file is opened in write mode,
the file's existing content is deleted.
The write method returns the number of bytes
written to a file, if successful.
"""
with open("newfile.txt") as f:
   print(f.read())
#in this way the original file is always closed

#classes----------------------------------------------------------
input('Classes')

class Cat:
  def __init__(self, color, legs): #method
    self.color = color
    self.legs = legs
  def bark(self):  #other method
    print("Woof!")

felix = Cat("ginger", 4)
print(felix.color)
felix.bark()

#Inheritance
class Animal:
  def __init__(self, name, color):
    self.name = name
    self.color = color
  def bark(self):
    print("Superclass")

class Cat(Animal):
  def purr(self):
    print("Purr...")

class Dog(Animal):
  def bark(self):
    print("Woof!") #stesse funzioni si sovrascrivono
    super().bark()#super(). call a method from the superclass

c=Cat("Minu", "gray")
c.purr()
Dog("Fido","white").bark()

"""
Magic methods are special methods which have double underscores at the beginning and end of their names.
They are also known as dunders.
So far, the only one we have encountered is __init__,
"""
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

"""
These allow to make operations between objects
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

"""

class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

"""
spam
============
Hello world!
"""
