import random
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
random.shuffle(deck)
nick = input('Enter your name: ')
print('Welcome to the Black Jack, ', nick)
count = 0
td1 = ''
while True:
    choice = input('Will you draw a card? y/n\n')
    if choice == 'y':
        td = deck.pop()
        if td == 11:
            td1 = 'Jack'
        elif td == 12:
            td1 = 'Queen'
        elif td == 13:
            td1 = 'King'
        elif td == 14:
            td1 = 'Ace'
        elif td < 11:
            td1 = td
        print('You have drawn a card with nominal of %s' % td1)
        count += td
        if count > 21:
            print('Sorry, you have lost.')
            choice1 = input('Do you want to play again? y/n\n')
            if choice1 == 'y':
                count = 0
                continue
            elif choice1 == 'n':
                break
        elif count == 21:
            print('Congratulations! You have exactly 21 points.')
            choice2 = input('Do you want to play again? y/n\n')
            if choice2 == 'y':
                count = 0
                continue
            elif choice2 == 'n':
                break
        else:
            print('You have %d point.' % count)
    elif choice == 'n':
        print('You had %d points.' % count, 'It\'s close enough. %d points to 21' % (21 - count))
        choice1 = input('Do you want to play again? y/n\n')
        if choice1 == 'y':
            count = 0
            continue
        elif choice1 == 'n':
            break

print('See you!')
