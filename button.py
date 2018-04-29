#!/usr/bin/env python3
import sys

batteries = None

def held_button():
    print("  HOLD AND RELEASE WHEN:")
    print("    Color\tTimer has _ in any position")
    print("    _____\t___________________________")
    print("    Blue\t4")
    print("    Yellow\t5")
    print("    Other\t1")

def batteries():
    if batteries==None:
        try:
            batteries = int(input("  # Batteries:\t").lower())
        except:
            batteries = None
            print("Invalid battery number")
            return -1
    return 0

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
                held_button()
            elif button[1]=='detonate':
                batteries()
                if batteries>1:
                    print("PRESS AND IMMEDIATELY RELEASE")
            elif button[0]=='w':
                print("  If lit indicator says CAR:")
            elif 
                

print("Button")
prompt_button()