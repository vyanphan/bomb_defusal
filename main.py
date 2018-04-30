#!/usr/bin/env python3

# import button as b
# import symbols as s
from bomb_defusal import *

def help_main():
    pass

def prompt_main():
    quit = False
    while not quit:
        user_input = input("[MODULE]\t").lower()
        print()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            help_main()
        elif user_input=="simple wires":
            simple_wires.prompt_simple_wires()
        elif user_input=="button":
            button.prompt_button()
        elif user_input=="symbols":
            symbols.prompt_symbols()
        print()

    

prompt_main()