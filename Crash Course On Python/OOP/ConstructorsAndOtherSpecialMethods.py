"""
In this code, there's a Person class that has an attribute name, which gets set when constructing the object.
Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 2)
when the greeting() method is called, the greeting states the assigned name.
"""
###################################

class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("José")
# Call the greeting method
print(some_person)

###################################
"""
Here is your output:
hi, my name is José
"""