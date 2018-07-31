high = 100
low = 0


def enter_answer():
    return input("Enter 'h' to indicate the guess is too high. "
               "Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")


def try_guess(high, low):
    guess = int((high - low) /2.0 + low)
    print("Is your secret number " + str(guess) + "?")
    return guess


print('Please think of a number between 0 and 100!')
guess = try_guess(high,low)
answer = enter_answer()

while True:
    while answer not in 'hlc':
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")
        answer = enter_answer()

    if answer == 'h':
        high = guess
        guess = try_guess(high, low)
        answer = enter_answer()

    elif answer == 'l':
        low = guess
        guess = try_guess(high, low)
        answer = enter_answer()

    elif answer == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
