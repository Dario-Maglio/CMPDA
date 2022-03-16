class Television:
    """ Class describing a televsion."""

    def __init__(self, owner):
        """ The special method __init__ is called each time a class istance is
        created. We can pass arguments to the constructor, just like any
        function."""
        print('Creating a television instance...')
        self.model = 'Sv32X-553T' # This class attribute is hard-coded
        self.owner = owner # This is set to the value of the argument

    def print_info(self): # Let’s see
        """ Print the model and owner"""
        message = 'This is television model {}, owned by {}'
        print(message.format(self.model, self.owner))

    NUMBER_OF_CHANNELS = 999 # This is a class attribute

my_television = Television('Alberto')
my_television.print_info()
batman_television = Television('Batman')
batman_television.print_info()

# Changing the attribute in the class namespace will change it for every instance
another_tv = Television('Alberto')
Television.NUMBER_OF_CHANNELS = 998
print(another_tv.NUMBER_OF_CHANNELS)
# But assigning to that attribute in an instance namespace will create a copy!
# Result: the other instances won’t be affected!
batman_television.NUMBER_OF_CHANNELS = 997
print(another_tv.NUMBER_OF_CHANNELS)

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
    self._x = x
    self._y = y

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

  def __eq__(self, other):
    return ((self.x, self.y)==(other.x, other.y))

  def __hash__(self):
    return (hash(self.x) ^ hash(self.y)

  def __repr__(self):
    class_name = type(self).__name__
    return ('{}({}, {})'.format(class_name, self.x, self.y))

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
print(result)
print(first==second)
print(hash(result))

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
