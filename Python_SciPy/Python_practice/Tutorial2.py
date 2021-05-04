print(r'C:Device\aaaa\name')
c=233.1234567788
print(c)
print(round(c,3))

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
     print(a)
     a, b = b, a+b

#a function can be called with an arbitrary number of arguments
def concat(*args, sep="/"):
     return sep.join(args)

    #args is a tuple and sep can be omitted in function call
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

#matrix

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
print(matrix)

print([[row[i] for row in matrix] for i in range(4)])
#or equivalently
transposed=[]
for i in range(4):
     transposed.append([row[i] for row in matrix])
print(transposed)

#loop method
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))

for i, v in enumerate(['tic', 'tac', 'toe']):
     print(i, v)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
     print(k, v)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
     print(f'{name:10} ==> {phone:10d}')

"""
If you have an object x, you can view its JSON string
representation with a simple line of code:
"""
import json
file = open("newfile.txt", "w")
# do stuff to the file
l=file.write("This has been written to a file\n")
file.write("This has been written to a file1\n")
file.write("This has been written to a file2\n")
l=file.write("This has been written to a file3\n")
for i in range(10):
     json.dump([i, i**2], file)
     file.write('\n')

file.write(json.dumps([123, 123.43, 'a']))
file.write('\n')
file.write(json.dumps([12,  'b']))
file.write('\n')
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

"""
Another variant of the dumps() function, called dump(),
simply serializes the object to a text file. So if f is a text file
object opened for writing, we can do this:
To decode the object again, if f is a text file object
which has been opened for reading:
"""

#f=open('newfile.txt', "r")
#f.read(4*l - 1)
#x = json.load(f)
#print (x)



