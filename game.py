# RANDOM GAME COLLECTION
""" A collection of games I've made along my coding journey.
The games appear in the order in which I created them, so the first one "number_guess" was the
 first attempt at coding really. """

import time

import number_guess
import hangman
import snap



def title():
    print("---------------------")
    print("----RANDOM GAMES ----")
    print("---------------------")


def main():
    title()
    time.sleep(1)
    print("""
    [N] Guess The Number
    [H] Hangman
    [S] Snap
    """)
    choice = input().upper()
    if choice == "N":
        number_guess.main()
    elif choice == "H":
        hangman.hangman()
    elif choice == "S":
        snap.snap()
    else:
        print("Invalid choice")
        main()

if __name__ == "__main__":
    main()