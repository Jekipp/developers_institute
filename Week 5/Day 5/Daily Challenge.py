class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name
        self.pen = {}

    def add_animal(self, new_animal)
        if self.animal != new_animal:
            self.animals.append(new_animal)

    def get_animal(self,animals):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        print(f'goodbye {animal_sold}')
        self.animals.remove(animal_sold)

    def sort_animal(self):
        for animal in self.animals:
            pen_number = ord(animal[0].upper) - 64
            if pen_number not in self.pen:
                self.pen.update({pen_number: animal})



zoo = Zoo("nyz zoo")
zoo.add_animal("cow")
zoo.add_animal("sheep")
zoo.sell_animal('cow')
