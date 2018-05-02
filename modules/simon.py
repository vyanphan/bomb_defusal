#!/usr/bin/env python3
from modules import globvars

color_map = {'r': ('b', 'y', 'g', 'b', 'r', 'y'),
             'b': ('r', 'g', 'r', 'y', 'b', 'g'),
             'g': ('y', 'b', 'y', 'g', 'y', 'b'),
             'y': ('g', 'r', 'b', 'r', 'g', 'r')}

def map_position():
    sn = globvars.get_serial_num()
    if 'a' in sn or 'e' in sn or 'i' in sn or 'o' in sn or 'u' in sn:
        return globvars.get_strikes()
    else:
        return globvars.get_strikes() + 3

def solve_simon(colors):
    i = map_position()
    try:
        ans = [color_map[c][i] for c in colors]
        print("  " + ' '.join(ans))
    except:
        print("  Incorrect color code!")

def simon_help():
    print("      <c><c><c><c>")
    print("      Enter color codes according to the table without spaces.")
    print("        Red      r")
    print("        Blue     b")
    print("        Green    g")
    print("        Yellow   y")
    print("      If asked for 'Serial#', enter serial number as-is.")
    print("      Type 'set <i>' to set a new #Strikes. Type 'set 0' to clear #Strikes.")
    print("      Type 'q' to quit or 'reset' to clear Serial# ONLY.")

def prompt_simon():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Color Codes:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            simon_help()
        elif user_input=="reset":
            globvars.set_serial_num(None)
        elif "set " in user_input:
            try:
                globvars.set_strikes(int(user_input[4:]))
            except BaseException:
                print("  Invalid number of strikes!")
        else:
            colors = [c for c in user_input]
            if globvars.get_serial_num()==None:
                globvars.set_serial_num(input("    {0:16}".format("Serial#:")).strip().lower())
            solve_simon(colors)
        print()
        