#!/usr/bin/env python3
from modules import global_vars

color_mapping = {'r': ('b', 'y', 'g', 'b', 'r', 'y'),
                 'b': ('r', 'g', 'r', 'y', 'b', 'g'),
                 'g': ('y', 'b', 'y', 'g', 'y', 'b'),
                 'y': ('g', 'r', 'b', 'r', 'g', 'r')}

def map_position(num_strikes):
    sn = global_vars.get_serial_num()
    if 'a' in sn or 'e' in sn or 'i' in sn or 'o' in sn or 'u' in sn:
        return num_strikes
    else:
        return num_strikes + 3

def prompt_simon():
    quit = False
    while not quit:
        user_input = input("  > Color Codes:\t").lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            print("      Red      r")
            print("      Blue     b")
            print("      Green    g")
            print("      Yellow   y")
        elif user_input=="reset":
            global_vars.set_serial_num(None)
        else:
            colors = [c for c in user_input]
            try:
                num_strikes = int(input("    Number of Strikes:\t"))
            except BaseException:
                global_vars.set_serial_num(None)
                global_vars.set_last_digit(None)
                print("  Invalid serial number!")

            if global_vars.get_serial_num()==None:
                global_vars.set_serial_num(input("    Serial Number:\t").lower())



        print()