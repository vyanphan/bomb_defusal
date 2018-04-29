#!/usr/bin/env python3
import sys

wires = []
serial_num = ''
last_digit = None

def prompt_serial_num():
    global serial_num
    global last_digit
    if serial_num=='':
        serial_num = input("  Serial Number:\t").lower()
    if last_digit==None:
        last_digit = int(serial_num[-1:])

wires = [c for c in input("Simple Wires:\t").lower()]

if len(wires)==3:
    if 'r' not in wires:
        print("2nd")
    elif wires[-1]=='w':
        print("last")
    elif wires.count('b')>1:
        print("last blue")
    else:
        print("last")

elif len(wires)==4:
    serial_num()    
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

elif len(wires)==5:
    prompt_serial_num()
    if wires[-1]=='k' and last_digit%2==1:
        print("4th")
    elif wires.count('r')==1 and wires.count('y')>1:
        print("1st")
    elif wires.count('k')==0:
        print("2nd")
    else:
        print("1st")

elif len(wires)==6:
    prompt_serial_num()
    if wires.count('y')==0 and last_digit%2==1:
        print("3rd")
    elif wires.count('y')==1 and wires.count('w')>1:
        print("4th")
    elif wires.count('r')==0:
        print("last")
    else:
        print("4th")

