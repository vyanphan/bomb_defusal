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

def ret_true():
    return True

def ret_false():
    return False

def ret_last_digit():
    return globvars.get_last_digit()%2==0

def ret_batteries():
    return globvars.get_batteries()>1

def ret_parallel_port():
    return globvars.get_parallel_port()

actions = {'0000': ret_true,
           '0001': ret_true,
           '0010': ret_last_digit,
           '0011': ret_false,
           '0100': ret_last_digit,
           '0101': ret_true,
           '0110': ret_last_digit,
           '0111': ret_parallel_port,
           '1000': ret_false,
           '1001': ret_batteries,
           '1010': ret_parallel_port,
           '1011': ret_parallel_port,
           '1100': ret_batteries,
           '1101': ret_batteries,
           '1110': ret_last_digit,
           '1111': ret_false}

def complicated_help():
    pass

def search(x, code):
    if x in code:
        return '1'
    else:
        return '0'

def translate(code):
    if code=='-':
        key = '0000'
    else:
        key = search('l', code)
        key += search('r', code)
        key += search('b', code)
        key += search('*', code)
    if actions[key]():
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
