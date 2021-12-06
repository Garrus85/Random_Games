#GUESS THE NUMBER
"""The very first "game" of my coding journey."""

import game
import random

def main():
    print("Welcome to Guess The Number!")
    print("You have 10 guesses to get it right!")
    print("\n")
    x = random.randint(0, 100)
    count = 0
    guess = 10

    while True:
        user = input("Please take a guess at what number I am thinking of between 0-100? ")
        try:
            iuser = int(user)
        except:
            print("Invalid number!")
            continue

        while count < 10:
            if iuser == x:
                print("Well done, you guessed correctly. The number I was thinking of was: ", str(x))
                cont = input("Would you like to play again? Y/N? ")
                print("\n")
                if cont in ("Y", "y", "yes", "yea", "yeah"):
                    main()
                else:
                    game.main()
            elif iuser > x:
                print("\n")
                print("Your guess is higher than the number I was thinking of!")
                count += 1
                guess = 10 - count
                if guess == 0:
                    print("You are out of guesses!")
                    print("\n")
                    main()
                else:
                    print("You only have", str(guess), "guesses left!")
                    user = input("Please have another guess? ")
                    try:
                        iuser = int(user)
                    except:
                        print("Invalid number!")
            else:
                print("\n")
                print("Your guess is lower than the number I was thinking of!")
                count += 1
                guess = 10 - count
                if guess == 0:
                    print("your are out of guesses!")
                    print("The number I was thinking of was ", int(x))
                    print("\n")
                    main()
                else:
                    print("You only have", str(guess), "guesses left!")
                    user = input("Please have another guess? ")
                    try:
                        iuser = int(user)
                    except:
                        print("Invalid number!")

