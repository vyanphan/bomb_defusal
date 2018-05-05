#!/usr/bin/env python3

'''
set UP = Left
relative positions

Read these positions

. . 2 3 4 .
. . 1 . . .

1101       = up
1100, 0101 = down
0001       = left
1111, 1110 = right
'''

pos_dict = {'1101': 'UP',
            '1100': 'DOWN',
            '0101': 'DOWN',
            '0001': 'LEFT',
            '1111': 'RIGHT',
            '1110': 'RIGHT'}

def prompt_knob():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("LEDs:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            wire_help()
        else:
            try:
                print('  ' + pos_dict[user_input])
            else:
                print('  Invalid LED positions!')
        print()