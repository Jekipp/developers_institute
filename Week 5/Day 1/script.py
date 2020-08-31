class Farm:
  def __init__(self, name):
    self.name = name
    self.animals = []

  def add_animal(self, animal, age):
    if animal in self.animals.keys():
      self.animals[animal] += number
  else:
      self.animals[animal] = number

farm = Farm('McDonald')
print(farm.animals)
farm.add_animal('cow', 5)
farm.add_animal('sheep')
print(farm.animal)

def get_info(self):
    output = f '{self.name}'s Farm\n'
    for animal, amount in self.animals.items():
        output += f"{animal} :{amount}\n"
        output += "   E - I - E - I - 0 !    "
        return output

def get_animal_types(self):
    return sorted(list(self.animals.keys()))
