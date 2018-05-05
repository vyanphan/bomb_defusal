#!/usr/bin/env python3

'''
only need the 1st 3 positions

<12345> <12345> <12345>
pos0    pos1    pos2

wordlist
prev = wordlist
curr = []

curr = [p for p in prev if p[i] in pos<i>]
prev = curr

print prev
'''

def password_help():
    print("      <x><x><x><x><x> <x><x><x><x><x> ...")
    print("      Enter all letters for each position. Separate positions with spaces.")
    print("      For maximum speed you can get away with entering as few as 3 positions.")
    print("      Type 'q' to quit.")

def prompt_password():
    pass
    