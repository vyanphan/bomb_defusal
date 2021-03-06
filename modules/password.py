#!/usr/bin/env python3

pswd_list = ['about', 'after', 'again', 'below', 'could',
             'every', 'first', 'found', 'great', 'house',
             'large', 'learn', 'never', 'other', 'place',
             'plant', 'point', 'right', 'small', 'sound',
             'spell', 'still', 'study', 'their', 'there',
             'these', 'thing', 'think', 'three', 'water',
             'where', 'which', 'world', 'would', 'write']

def password_help():
    print("      <x><x><x><x><x> <x><x><x><x><x> ...")
    print("      Enter all letters for each position. Separate positions with spaces.")
    print("      For maximum speed you can get away with entering fewer positions.")
    print("      Type 'q' to quit.")

def password_solve(letters):
    prev = list(pswd_list)
    curr = []
    for i in range(len(letters)):
        curr = [p for p in prev if p[i] in letters[i]]
        prev = curr
    return [c.upper() for c in curr]

def prompt_password():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Letter Combos:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            password_help()
        else:
            letters = user_input.split(' ')
            print('  ' + ', '.join(password_solve(letters)))
        print()
    