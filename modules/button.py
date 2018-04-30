#!/usr/bin/env python3
from modules import global_vars as global_vars

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
    elif color=='black':
        color = 'k'
    label = button[1]
    return color, label

def prompt_held_button():
    print("    HOLD AND RELEASE WHEN:")
    print("      Color\tTimer has x in any position")
    print("      ──────\t───────────────────────────")
    print("      Blue\t4")
    print("      Yellow\t5")
    print("      Other\t1")

def prompt_batteries():
    if global_vars.get_batteries()==None:
        try:
            global_vars.set_batteries(int(input("    Num Batteries:\t").lower()))
        except:
            global_vars.set_batteries(None)
            print("  Invalid battery number")
            return -1
    return global_vars.get_batteries()

def prompt_indicator():
    if global_vars.get_indicator()==None:
        global_vars.set_indicator(input("    Lit Indicator:\t").upper())
    return global_vars.get_indicator()

def prompt_button():
    quit = False
    while not quit:
        user_input = input("  > Color Label:\t").lower()
        if user_input == "q":
            quit = True
        elif user_input == "help":
            print("      Red      r")
            print("      Blue     b")
            print("      Yellow   y")
            print("      White    w")
            print("      Black    k")
        elif user_input == "reset":
            global_vars.set_batteries(None)
            global_vars.set_indicator(None)
        else:
            color, label = parse_input(user_input)
            if color==None or label==None:
                pass
            elif color=='b' and label=='abort':
                prompt_held_button()
            elif prompt_batteries()==-1:
                pass
            elif label=='detonate' and prompt_batteries()>1:
                print("  PRESS AND IMMEDIATELY RELEASE")
            elif color=='w' and prompt_indicator()=="CAR":
                prompt_held_button()
            elif prompt_batteries()>2 and prompt_indicator()=="FRK":
                print("  PRESS AND IMMEDIATELY RELEASE")
            elif color=='y':
                prompt_held_button()
            elif color=='r' and label=='hold':
                print("  PRESS AND IMMEDIATELY RELEASE")
            else:
                prompt_held_button()
        print()
