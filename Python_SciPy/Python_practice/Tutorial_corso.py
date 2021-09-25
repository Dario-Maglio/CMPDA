"""Tutorial from cours lessons."""

def func(**kwargs):
    """ Arbitrary number of optional arguments."""
    print(kwargs.get('verbose', False))

func()
func(verbose=True)
func(verbose=False)
func(verbose=True, num_events=3)
#func(True) this raise an error

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

#>>> greet_me(name="yasoob")
#name = yasoob

#----------------------------------------------------
list1 = [k**2 for k in range(2, 8)]
list2 = [k + 3 for k in list1]

# Nice-looking.
for i, item in enumerate(list1):
    print(i, item)
# Zipping iterables
for item1, item2 in zip(list1, list2):
    print(item1, item2)
# List comprehension
print([x**2 for x in list2])

#----------------------------------------------------

def parse_line(line):
    """ Parse a line of the file and return the values as float"""
    values = line.strip('\n').split(' ')
    # the following two lines may generate exceptions if they fails!
    time = float(values[0])
    tension = float(values[1])
    return time, tension

file_path = 'snippets/data/fake_measurements.txt'

try:
    with open(file_path) as lab_data_file:
        for line in lab_data_file:
            if not line.startswith('#'): # skip comments
                time, tension = parse_line(line)
            print(time, tension)
except FileNotFoundError:
    pass

# Pythonic way - you should prefer this one!
try:
    data_file = open(file_path)
except OSError as e: # Cover more problems than FileNotFoundError
    print('Oops - cannot read the file!\n{}'.format(e))

#--------------------------------------------------------

numbers = range(10)
squares = list(map(lambda n: n**2, numbers))
print(squares)

# Generator function that provides infinte fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# We need to impose a stop condition externally to use it
max_n = 7
fib_numbers = []
for i, fib in enumerate(fibonacci()):
    if i >= max_n:
        break
    else:
        fib_numbers.append(fib)
print(fib_numbers)
