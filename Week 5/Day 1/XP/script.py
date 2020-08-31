class Cat(self, name, age):
    def _init_(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Kitty", 2, "mammal")
cat2 = Cat("Panda", 3, "mammal")
cat3 = Cat("Cathandra", 4, "mammal")

def biggest_cat():
    if cat1.age > cat2.age and cat3.age:
        return cat1
    elif cat2.age > cat1.age and cat2.age:
        return cat2
    else:
        return cat3

big_cat = biggest_cat(cat1, cat2, cat3)
print(big_cat.name + "is the biggest")
