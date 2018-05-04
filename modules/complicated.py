#!/usr/bin/env python3
from modules import globvars

'''
    lrb*        = light red blue star
    (1 1 1 1)   = 15 = D
    r*          = red star
    (0 1 0 1)   =  5 = C
 
    > lrb* r* b*
    CUT 1 4 5 
'''

actions = {'0000': True,
           '0001': True,
           '0010': globvars.get_last_digit()%2==0,
           '0011': False,
           '0100': globvars.get_last_digit()%2==0,
           '0101': True,
           '0110': globvars.get_last_digit()%2==0,
           '0111': globvars.get_parallel_port(),
           '1000': False,
           '1001': globvars.get_batteries()>1,
           '1010': globvars.get_parallel_port(),
           '1011': globvars.get_parallel_port(),
           '1100': globvars.get_batteries()>1,
           '1101': globvars.get_batteries()>1,
           '1110': globvars.get_last_digit()%2==0,
           '1111': False}

def complicated_help():
    pass

def search(x, code):
    if x in code:
        return '1'
    else:
        return '0'

def translate(code):
    key = search('l', code)
    key += search('r', code)
    key += search('b', code)
    key += search('*', code)
    if actions[key]:
        return 'X'
    else:
        return '_'

def prompt_complicated():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Wire Codes:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            complicated_help()
        elif user_input=="reset":
            globvars.set_serial_num(None)
            globvars.set_last_digit(None)
            globvars.set_batteries(None)
            globvars.set_parallel_port(None)
        else:
            wires = [translate(c) for c in user_input.split(' ')]
            print("  " + ' '.join(wires))
        print()
