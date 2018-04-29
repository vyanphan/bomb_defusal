#!/usr/bin/env python3
import sys

serial_num = None
last_digit = None

def wires_3(wires):
    if 'r' not in wires:
        print("2ND")
    elif wires[-1]=='w':
        print("LAST")
    elif wires.count('b')>1:
        print("LAST BLUE")
    else:
        print("LAST")

def wires_4(wires):
    if wires.count('r')>1 and prompt_serial_num()%2==1:
        print("LAST RED")
    elif wires[-1]=='y' and wires.count('r')==0:
        print("1ST")
    elif wires.count('b')==1:
        print("1ST")
    elif wires.count('y')>1:
        print("LAST")
    else:
        print("2ND")

def wires_5(wires):
    if wires[-1]=='k' and prompt_serial_num()%2==1:
        print("4TH")
    elif wires.count('r')==1 and wires.count('y')>1:
        print("1ST")
    elif wires.count('k')==0:
        print("2ND")
    else:
        print("1ST")

def wires_6(wires):
    if wires.count('y')==0 and prompt_serial_num()%2==1:
        print("3RD")
    elif wires.count('y')==1 and wires.count('w')>1:
        print("4TH")
    elif wires.count('r')==0:
        print("LAST")
    else:
        print("4TH")

def prompt_serial_num():
    global serial_num
    global last_digit
    if serial_num==None:
        serial_num = input("  Serial #:\t").lower()
    if last_digit==None:
        try:
            last_digit = int(serial_num[-1:])
        except BaseException:
            serial_num = None
            last_digit = None
            print("Invalid serial number!")
            return 0
    return last_digit

def prompt_wires():
    global serial_num
    global last_digit
    quit = False
    while not quit:
        user_input = input("> Color codes:\t").lower()
        if user_input=="help":
            print("    Red      r")
            print("    Blue     b")
            print("    Yellow   y")
            print("    White    w")
            print("    Black    k")
        elif user_input=="q":
            quit = True
        elif user_input=="reset":
            serial_num = None
            last_digit = None
        else:
            wires = [c for c in user_input]
            if len(wires)==3:
                wires_3(wires)
            elif len(wires)==4:
                wires_4(wires)
            elif len(wires)==5:
                wires_5(wires)
            elif len(wires)==6:
                wires_6(wires)
        print()

print("Simple Wires")
prompt_wires()