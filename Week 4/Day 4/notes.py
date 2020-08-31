# reusable block of code
# input/argument | logic/operations | return/output
# first step: Definition
# second step: call funtion
# def func(arguments):
#  output = do_something_with(arguement)
#  return
# positional function add(1,2)
# keyword



def_average(l):
  avg = sum(l) / len (l)
  return avg

  avg = average([1, 2, 3, 4, 5, 6, 7, 8])

def say_hello():
    print("hello")

def add(x,y):
    return x + y

print(add(2,2))

def is_even(num):
    return num % 2 == 0

def even_number(l):
    evens = [num for num in l if is_even(num)]
    return evens

print(even_number([1,2,3,4,5,6,7,8,9]))


def say_hello(name = 'Jon'): #(default value)
    print(f'Hello {name}')

def say_hello(name1 = 'Jon', name2 = 'Ben'): #(default value)
    print(f'Hello {name1} and {name2}')

say_hello()
say_hello(name = 'Ben')


def my_name(name):
    first, last = name.split(" ")
    return first, last

name = my_name('Panda Kay')
    print(name)


#scope
def some_func(arg1, arg2):
    some variables = 10


def myinfo(**kwargs):
    for key in kwargs.keys():
        print(f'Your {key} is {kwargs[key]})
    return kwargs

print(myinfo(first_name = 'Jason', middle_name = 'E', last_name = 'Kipp', age = 33, profession = 'Developer'))

 d = dict(first_name = 'Jason', middle_name = 'E', last_name = 'Kipp', age = 33, profession = 'Developer')
