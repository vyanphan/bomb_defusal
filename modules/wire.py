#!/usr/bin/env python3
from modules import globvars

def wire_3(wires):
    if 'r' not in wires:
        print("  2ND")
    elif wires[-1]=='w':
        print("  LAST")
    elif wires.count('b')>1:
        print("  LAST BLUE")
    else:
        print("  LAST")

def wire_4(wires):
    if globvars.get_last_digit()<0:
        print("  Invalid serial number!")
    elif wires.count('r')>1 and globvars.get_last_digit()%2==1:
        print("  LAST RED")
    elif wires[-1]=='y' and wires.count('r')==0:
        print("  1ST")
    elif wires.count('b')==1:
        print("  1ST")
    elif wires.count('y')>1:
        print("  LAST")
    else:
        print("  2ND")

def wire_5(wires):
    if globvars.get_last_digit()<0:
        print("  Invalid serial number!")
    elif wires[-1]=='k' and globvars.get_last_digit()%2==1:
        print("  4TH")
    elif wires.count('r')==1 and wires.count('y')>1:
        print("  1ST")
    elif wires.count('k')==0:
        print("  2ND")
    else:
        print("  1ST")

def wire_6(wires):
    if globvars.get_last_digit()<0:
        print("  Invalid serial number!")
    elif wires.count('y')==0 and globvars.get_last_digit()%2==1:
        print("  3RD")
    elif wires.count('y')==1 and wires.count('w')>1:
        print("  4TH")
    elif wires.count('r')==0:
        print("  LAST")
    else:
        print("  4TH")

def wire_help():
    print("      <c><c><c>...<c>")
    print("      Enter color codes according to the table without spaces.")
    print("        Red      r")
    print("        Blue     b")
    print("        Yellow   y")
    print("        White    w")
    print("        Black    k")
    print("      If asked for 'Serial#', enter serial number as-is.")
    print("      Type 'q' to quit or 'reset' to clear Serial#.")

def prompt_wire():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Color Codes:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            wire_help()
        elif user_input=="reset":
            globvars.set_serial_num(None)
            globvars.set_last_digit(None)
        else:
            wires = [c for c in user_input]
            if len(wires)==3:
                wire_3(wires)
            elif len(wires)==4:
                wire_4(wires)
            elif len(wires)==5:
                wire_5(wires)
            elif len(wires)==6:
                wire_6(wires)
        print()
