#!/usr/bin/env python3
from modules import *

mods_list = ["Wires", "Button", "Keypads", "Simon Says", "Who's on First", "Memory", "Morse Code",
             "Complicated Wires", "Wire Sequences", "Mazes", "Passwords", "Knobs"]

def help_main():
    print("Type 'q' within a module to quit a single module, or in the main prompt to exit the \
           whole program.")
    print("Type 'help all' to view a list of the possible modules.")
    print("Type 'reset' within a module to reset the specific global variables related to that \
           particular module only, or in the main prompt to reset everything.")

def help_all():
    for m in mods_list:
        print("  " + m)


def prompt_main():
    quit = False
    while not quit:
        user_input = input("[MODULE] ").lower()
        print()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            help_main()
        elif user_input=="help all":
            help_all()
        elif user_input=="reset":
            global_vars.reset_all()
        elif user_input in {"wire", "wires", "simple wire", "simple wires", "simple"}:
            simple_wires.prompt_simple_wires()
        elif user_input in {"button", "buttons"}:
            button.prompt_button()
        elif user_input in {"keypad", "keypads", "symbol", "symbols"}:
            symbols.prompt_symbols()
        
        print()

prompt_main()