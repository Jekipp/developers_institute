family_list = [{'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False} ]


class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, new_name):
        new_baby = {
        'name' : new_name,
        'age' : 0,
        'is_child' : True,
        }

        self.members.append(new_baby)
        print('congrats on the new member')

    def is_18(self):
        for member in self.members:
            age = member['age']
            if age > 18:
                print(f"{member['name']} is over 18")
            else:
                print(f"{member['name']} is under 18")


my_family = Family(family_list, 'K')
my_family.born('Panda')
my_family.is_18()
