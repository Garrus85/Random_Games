import time

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
    [H] Hangman
    [S] Snap
    """)
    choice = input().upper()
    if choice == "H":
        hangman.hangman()
    elif choice == "S":
        snap.snap()
    else:
        print("Invalid choice")
        main()

if __name__ == "__main__":
    main()