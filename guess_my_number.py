high = 100
low = 0

print('Please think of a number between 0 and 100!')
guess = int((high - low)/2.0 + low)
print("Is your secret number " + str(guess) + "?")
answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while True:
    while answer not in 'hlc':
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if answer == 'h':
        high = guess
        guess = int((high - low) /2.0 + low)
        print("Is your secret number " + str(guess) + "?")
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    elif answer == 'l':
        low = guess
        guess = int((high - low)/2.0 + low)
        print("Is your secret number " + str(guess) + "?")
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    elif answer == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
