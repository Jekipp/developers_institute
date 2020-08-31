list
a_list = [1,2,"uy"]
convert something into a list
the_tuple = (1, 2, 3, "hi")
tuple_to_list = list(the_tuple)

for element in a_list:
    print(element_in_list)

add something to a list
a_list.append("add this")

string = "the good, the bad, the ugly"

string.split(", ")
# splits string with space and comma
list(string)
# converts every character into a list

indexing
get element at position i

a_list[i]
a_list[0]
# 1


dictionary
Dictionary = {"my_name" : "George", "my_age" : 27}
{key : value}

dictionary["my_name"]
# George

adding a key:
dictionary["height"] = 1.70

if "height" in dictionary.keys():
    # True
if "George" in dictionary.values():
    # True
dictionary['my_name']

users = {"user1" : {'name' : 'George', 'age' : 25}, "user1" : {'name' : 'Panda', 'age' : 5}}
for user in users.key()
    info = users[user]
    name = info['name']
    if name == 'George'
        print(info)
# prints dictionary

for users in users.key():
    info = users[user]
    if "power" not in info.key():
        continue
    power = info['power']
    if power = info['power']
    if power == 'strength':
        print(info)


functions

def name_of_function(arguement1, arguement2, ... )
    return

def multiply(num1, num2)
    return num1 * num2

save = multiply(2, 3)


magician_list = ['Houdini', 'Harry', 'Mysterio']

def show_magicians(list):
    for i in list
    return i

def make_great(show_magicians):
    for i in range(len(magician_list)):
        magician_list =  'the great' + magician_list[i]

show_magicians(magician_list)


functonal programming vs object oriented programming




class Bank_account(self, owner, balance):
    def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money

    def withdraw():
        if self.balance > money:
            self.balance -= money
        else:
            print('insufficeint funds')
    return balance


class Owner(Bank_account):
    def __init__(self, owner, balance, cc_number, password)
    super(). __init__(owner, balance)
    self.cc_number = cc_number
    self.password = password

    def check_owner_info(self):
        for i in range(2):
            pw = int(input("credit card pw?"))
            if self.password == pw
                answer = input('withdraw or deposit?')
                if answer = "deposit":
                    money = int(input("money: "))
                    self.deposit(money)
                    return
                elif:
                    money = int(input("money: "))
                    self.withdraw(money)
                    return
                else:
                    print('I dont understand')
        else:
            print("1 more chance")
    print('eat card')
