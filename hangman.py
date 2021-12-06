# GAME 1: HANGMAN
""" My first attempt at coding a game """

import random


def success():

    print("Well done, you have saved the man!")
    again = input("Would you like to play again? Y/N")
    if again in ["y", "Y", "YES", "Yes"]:
        hangman()
    else:
        print("---------- Thanks for playing ----------")
    quit()


def hangman():

    print("""------------ \
          WELCOME TO HANGMAN \
           ------------""")

    """ Ask the user to choose a category """

    choice = input("What category do you want? Games (G) or Movies (M)")
    if choice in ["games", "Games", "G", "game", "Game", "g"]:
        file = open("games.txt", "r")
        line = file.readline()
    elif choice in ["movies", "Movies", "M", "m", "movie", "Movie"]:
        file = open("movies.txt", "r")
        line = file.readline()
    else:
        print("Invalid input, please try again")

    """ read the file containing the category for the game """
    items = []
    while line:
        clean_line = line[:-1]
        items.append(clean_line)
        line = file.readline()
        if line == "":
            break
        else:
            continue
    file.close()

    """ Randomly choose an item for the game """
    size = len(items)
    random_choice = random.randint(0, (size-1))
    selection = items[random_choice]
    game_word = ""
    for item in selection:
        for char in item:
            game_word = game_word + char.lower()

    """hangman game logic"""
    blank = "_ "
    hidden_word = ""
    for char in game_word:
        if char == " ":
            hidden_word = hidden_word + "/"
        else:
            hidden_word = hidden_word + blank

    letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]

    n = len(game_word) + 2
    while n > 0:
        print(hidden_word)
        print("Your have " + str(n) + " guesses left!")
        revealing_word = ""
        guess = input("Guess a letter?")
        try:
            if guess in letterlist:
                letterlist.remove(guess)
        except:
            print("Invalid input or letter already used, please choose another letter")
            continue

        for letter in game_word:
            if letter == " ":
                revealing_word = revealing_word + "/"
            elif letter not in letterlist:
                revealing_word = revealing_word + letter
            else:
                revealing_word = revealing_word + blank
        print(revealing_word)

        """let the user guess the word"""
        take_a_guess = input("Would you like to guess the answer?")
        if take_a_guess in ["Y", "y", "YES", "yes", "Yes"]:
            word_guess = input("What do you think the answer is?")
            if word_guess == game_word:
                success()

        """ check if hangman is completed or not """
        if blank not in revealing_word:
            success()
        else:
            n = n - 1
            hidden_word = revealing_word  # reinitialise hidden_word before while loop continues
            continue

    if n == 0:
        print("You failed. The answer was " + game_word)
        again = input("Would you like to play again? Y/N")
        if again in ["y", "Y", "YES", "Yes"]:
            hangman()
        else:
            print("---------- Thanks for playing ----------")
