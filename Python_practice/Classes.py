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
