matrix = [
    [7, " ", 3],
    ["T", "s", "i"],
    ["i", " ", "x"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["i", "r", "!"],
]
#for each row get position 1
#each row position 2
#row position 3

#loop through the rows
#Loop through positional
#col: 0 row: 1 - 8

text = ' '
symbol = ''
for col in range(3):
    for row in matrix:
        char = row[col]
        if type(char) is str and char.isalnum():
            text += char
        else:
            text += char
            
print(text)

finaltext = ''

for i in range(len(text)):
    first_letter = text [i]
    second_letter = text[i + 1]
