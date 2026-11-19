class Area:

  # special function for setting up new 'instances' of the class. 
  def __init__(self, name):
    # variable 'self' refers to the Area instance being initialised,
    # and is always the first function parameter on class functions.
    self.name = name
    self.paths = []  # will contain other Area instances

  def leads_to(self, new_paths):
    self.paths = new_paths

# create two instances of Area
town = Area("south shields")  # calls __init__ function
slums = Area("jarrow")

town.leads_to([slums])  # list containing one 'Area'

print("first path outta town:", town.paths[0].name)