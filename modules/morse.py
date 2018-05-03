#!/usr/bin/env python3

morse_dict = {'.-'  : 'a',
              '-...': 'b',
              '-.-.': 'c',
              '-..' : 'd',
              '.'   : 'e',
              '..-.': 'f',
              '--.' : 'g',
              '....': 'h',
              '..'  : 'i',
              '.---': 'j',
              '-.-' : 'k',
              '.-..': 'l',
              '--'  : 'm',
              '-.'  : 'n',
              '---' : 'o',
              '.--.': 'p',
              '--.-': 'q',
              '.-.' : 'r',
              '...' : 's',
              '-'   : 't',
              '..-' : 'u',
              '...-': 'v',
              '.--' : 'w',
              '-..-': 'x',
              '-.--': 'y',
              '--..': 'z'}

freq_dict = {'she': '  3.505 MHz',
             'hal': '  3.515 MHz',
             'sli': '  3.522 MHz',
             'tri': '  3.532 MHz',
             'box': '  3.535 MHz',
             'lea': '  3.542 MHz',
             'str': '  3.545 MHz',
             'bis': '  3.552 MHz',
             'fli': '  3.555 MHz',
             'bom': '  3.565 MHz',
             'bre': '  3.572 MHz',
             'bri': '  3.575 MHz',
             'ste': '  3.582 MHz',
             'sti': '  3.592 MHz',
             'vec': '  3.595 MHz',
             'bea': '  3.600 MHz'}

def morse_help():
    print("      <m> <m> <m>")
    print("      Enter '-' for dash and '.' for dot. Separate letters with spaces.")
    print("      Only the first 3 letters are required for a unique answer.")
    print("      Type 'q' to quit.")

def prompt_morse():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Morse Code:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            morse_help()
        else:
            morse = user_input.split(' ')[:3]
            word = ''.join([morse_dict[m] for m in morse])
            print(freq_dict[word])
        print()
