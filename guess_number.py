#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program allows user to guess number


import constants


def main():
    # I check if the user guessed correctly

    # input
    guess = int(input("Guess a number between 0-9: "))

    # process&output
    if constants.CHOSEN_NUMBER == guess:
        print("You got it!")
    if constants.CHOSEN_NUMBER != guess:
        print("Maybe next time!")

    print("\nDone.")


if __name__ == "__main__":
    main()
