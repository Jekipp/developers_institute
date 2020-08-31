
jack = {
"suit" : "royal",
"name" : "J",
"number" : 1
}
queen = {
"suit" : "royal",
"name" : "Q",
"number" : 2
}
king = {
"suit" : "royal",
"name" : "K",
"number" : 3
}


hand1 =[jack, queen, king]
hand2 =[jack, jack, queen, king]
total_hand1 = 0
total_hand2 = 0
total = 0

for card in hand1:
    total_hand1 += card["number"]
print(total_hand1)

for card in hand2:
    total_hand2 += card["number"]
print(total_hand2)



courts = [hand1, hand2]
totals = []

for hand in courts:
    temp_total = 0
    for card in hand:
            temp_total += card['number']
            totals.append(temp_total)

if totals[0] > totals[1]:
        print('player 1 wins')

elif totals[1] > totals[0]:
        print('player 2 wins')

else:
    print('draw')
