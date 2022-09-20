"""
Let’s create a new class together and inherit from it. Below we have a base class called Clothing.
Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. 
Fill in the blanks to make it work properly.
"""
##############################

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {name} is made of {material}".format(name=self.name, material=self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

##############################

"""
Here is your output:
This Polo is made of Cotton
"""