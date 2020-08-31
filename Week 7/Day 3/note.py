class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

    def say_hi(self):
      print(f'Hello, my name is {self.my_name}')

p1 = Person('Jon', 5)
p2 = Person('Jane', 6)



class BankAccount():
  def __init__(self, owner_name)
    self.owner_name = owner_name
    self.balanace = 0
