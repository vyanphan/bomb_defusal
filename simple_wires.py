#!/usr/bin/env python3

# give prompt for wires

# receive prompt (toLowerCase)
input = ''

# parse colors


wires = []
serial_num = ''
last_digit = None

if len(wires)==3:
	if 'r' not in wires:
        print("2nd")
    elif wires[-1]=='w':
        print("last")
    elif wires.count('b')>1:
        print("last blue")
    else
        print("last")

elif len(wires)==4:
    if serial_num=='':
        # prompt for serial num
        # receive serial num toLowerCase
    if last_digit==None:
        last_digit = int(serial_num[-1:])
    
    if wires.count('r')>1 and last_digit%2==1:
        print("last red")
    elif wires[-1]=='y' and wires.count('r')==0:
        print("1st")
    elif wires.count('b')==1:
        print("1st")
    elif wires.count('y')>1:
        print("last")
    else
        print("2nd")

elif len(wires)==5:
    if serial_num=='':
        # prompt for serial num
        # receive serial num toLowerCase
    if last_digit==None:
        last_digit = int(serial_num[-1:])

    if wires[-1]=='k' and last_digit%2==1:
        print("4th")
    elif wires.count('r')==1 and wires.count('y')>1:
        print("1st")
    elif wires.count('k')==0:
        print("2nd")
    else
        print("1st")

elif len(wires)==6:
    if serial_num=='':
        # prompt for serial num
        # receive serial num toLowerCase
    if last_digit==None:
        last_digit = int(serial_num[-1:])

    if wires.count('y')==0 and last_digit%2==1:
        print("3rd")
    elif wires.count('y')==1 and wires.count('w')>1:
        print("4th")
    elif wires.count('r')==0:
        print("last")
    else
        print("4th")

