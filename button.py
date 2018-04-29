#!/usr/bin/env python3
import sys

def held_button():
    print()

def prompt_button():
    quit = False
    while not quit:
        user_input = input("Color Label:\t").lower()
        if user_input == "help":
            print("  Red\tr\n  Blue\tb\n  Yellow\ty\n  White\tw\n  Black\tk\n")
        elif user_input == "q":
            quit = True


print("Button")
prompt_button()