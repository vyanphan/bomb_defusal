#!/usr/bin/env python3

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
           '0010': get_last_digit()%2==0,
           '0011': False,
           '0100': get_last_digit()%2==0,
           '0101': True,
           '0110': get_last_digit()%2==0,
           '0111': has_parallel_port(),
           '1000': False,
           '1001': get_batteries()>1,
           '1010': has_parallel_port(),
           '1011': has_parallel_port(),
           '1100': get_batteries()>1,
           '1101': get_batteries()>1,
           '1110': get_last_digit()%2==0,
           '1111': False}

def prompt_complicated():
    pass
