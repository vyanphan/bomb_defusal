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

def knob_help():
    print("      <#><#><#><#>")
    print("      Enter LEDs in the following order, 1 for on and 0 for off.")
    print("        . . 2 3 4 .")
    print("        . . 1 . . .")
    print("      You only need 4 LEDs; don't bother with the others.")
    print("      Type 'q' to quit.")

def prompt_knob():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("LED Codes:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            knob_help()
        else:
            try:
                print('  ' + pos_dict[user_input])
            except:
                print('  Invalid LED positions!')
        print()