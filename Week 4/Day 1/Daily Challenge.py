import random

num = input("please enter a charachter string")
if len(num) != 10:
    num = input("not 10 charachters long")
else:
    print(f"the first letter is {num[0]}")
    print(f"the last letter is {num[-1]}")
    for i in range(len(num)+1):
        print(num[:i])

shuffled = list(num)
random.shuffle(shuffled)
shuffled = "".join(shuffled)
print(shuffled)
