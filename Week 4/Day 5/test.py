text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris isi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit sse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt n culpa qui officia deserunt mollit anim id est laborum."""
#write a function that gives the number of words
#write a function that takes a letter, and counts the occurrances of that letter

length = len(text.split())
print(length)


##char = input("return letter")
user_letter = input("return letter")


def count_char(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    print(count)
count_char(text, user_letter)



counter = text.count('a')
print(counter)
