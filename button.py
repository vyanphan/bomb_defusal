#!/usr/bin/env python3
import sys

batteries = None

def held_button():
    print("  Hold the button and release when:")

    print("  Blue\t")

def prompt_button():
    global batteries
    quit = False
    while not quit:
        user_input = input("> Color Label:\t").lower()
        if user_input == "help":
            print("    Red      r")
            print("    Blue     b")
            print("    Yellow   y")
            print("    White    w")
            print("    Black    k")
        elif user_input == "q":
            quit = True
        else:
            button = user_input.split(' ')
            if button[0]=='b' and button[1]=='abort':
            elif button[1]=='detonate':

                try:
                    batteries = int(input("  # Batteries:\t").lower())
                except:
                    batteries = None
                    print("Invalid battery number")

print("Button")
prompt_button()