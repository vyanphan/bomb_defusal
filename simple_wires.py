#!/usr/bin/env python3
import sys

serial_num = ''
last_digit = None

def wires_3(wires):
    if 'r' not in wires:
        print("2nd")
    elif wires[-1]=='w':
        print("last")
    elif wires.count('b')>1:
        print("last blue")
    else:
        print("last")

def wires_4(wires):
    prompt_serial_num()    
    if wires.count('r')>1 and last_digit%2==1:
        print("last red")
    elif wires[-1]=='y' and wires.count('r')==0:
        print("1st")
    elif wires.count('b')==1:
        print("1st")
    elif wires.count('y')>1:
        print("last")
    else:
        print("2nd")

def wires_5(wires):
    prompt_serial_num()
    if wires[-1]=='k' and last_digit%2==1:
        print("4th")
    elif wires.count('r')==1 and wires.count('y')>1:
        print("1st")
    elif wires.count('k')==0:
        print("2nd")
    else:
        print("1st")

def wires_6(wires):
    prompt_serial_num()
    if wires.count('y')==0 and last_digit%2==1:
        print("3rd")
    elif wires.count('y')==1 and wires.count('w')>1:
        print("4th")
    elif wires.count('r')==0:
        print("last")
    else:
        print("4th")

def prompt_serial_num():
    global serial_num
    global last_digit
    if serial_num=='':
        serial_num = input("  Serial Number:\t").lower()
    if last_digit==None:
        last_digit = int(serial_num[-1:])

def prompt_wires():
    quit = False
    while not quit:
        user_input = input("Simple Wires:\t").lower()
        if user_input == "help":
            print("Red\tr\nBlue\tb\nYellow\ty\nWhite\tw\nBlack\tk\n")
        elif user_input == "q":
            quit = True
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

prompt_wires()