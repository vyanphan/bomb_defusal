#!/usr/bin/env python3
from modules import globvars

def parse_input(user_input):
    button = user_input.lower().split(' ')
    if len(button) != 2:
        return None, None
    color = button[0]
    if color=='red':
        color = 'r'
    elif color=='blue':
        color = 'b'
    elif color=='yellow':
        color = 'y'
    elif color=='white':
        color = 'w'
    label = button[1]
    return color, label

def prompt_held_button():
    print("  HOLD AND RELEASE WHEN:")
    print("    {0:8}{1}".format("Color", "Timer has x in any position"))
    print("    " + "─" * 35)
    print("    {0:8}{1}".format("Blue", "4"))
    print("    {0:8}{1}".format("Yellow", "5"))
    print("    {0:8}{1}".format("Other", "1"))

def button_help():
    print("      <c> <label>")
    print("      Enter color code according to the table, 1 space, then button label as-is.")
    print("        {0:17}{1}".format("Red", "r"))
    print("        {0:17}{1}".format("Blue", "b"))
    print("        {0:17}{1}".format("Yellow", "y"))
    print("        {0:17}{1}".format("White", "w"))
    print("        {0:17}{1}".format("Any other color", "x"))
    print("      Enter a number for #Batteries.")
    print("      Enter all Indicator labels as-is, separated by spaces.")
    print("      Type 'q' to quit or 'reset' to clear #Batteries and Indicator.")

def prompt_button():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Color Label:")).strip().lower()
        if user_input == "q":
            quit = True
        elif user_input == "help":
            button_help()
        elif user_input == "reset":
            globvars.set_batteries(None)
            globvars.set_indicator(None)
        else:
            color, label = parse_input(user_input)
            if color==None or label==None:
                pass
            elif color=='b' and label=='abort':
                prompt_held_button()
            elif globvars.get_batteries()==-1:
                print("  Invalid battery number!")
            elif label=='detonate' and globvars.get_batteries()>1:
                print("  PRESS AND IMMEDIATELY RELEASE")
            elif color=='w' and "CAR" in globvars.get_indicator():
                prompt_held_button()
            elif globvars.get_batteries()>2 and "FRK" in globvars.get_indicator():
                print("  PRESS AND IMMEDIATELY RELEASE")
            elif color=='y':
                prompt_held_button()
            elif color=='r' and label=='hold':
                print("  PRESS AND IMMEDIATELY RELEASE")
            else:
                prompt_held_button()
        print()
