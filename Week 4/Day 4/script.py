year = input("what is your birthyear YYYY: ")

def get_age(): 
    age = 2020 - int(year)
    return age
get_age()

def can_retire(age):
    age = get_age()
    if int(age) > 60:
        print("Retiree")
    else:
        print("Citizen")
can_retire(year)
