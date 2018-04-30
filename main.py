#!/usr/bin/env python3

import button as b
import symbols as s

def prompt_main():
    quit = False
    while not quit:
        user_input = input("> Module:\t").lower()
        if user_input=="q":
            quit = True
        elif user_Input=="help":

        elif user_input=="simple wires":

        elif user_input=="button":

        elif user_input=="symbols":
            s.prompt_symbols()

        print()


    

prompt_main()