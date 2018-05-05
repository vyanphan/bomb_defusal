#!/usr/bin/env python3

'''
colors:     r   b   k

<c><pos> <c><pos> ...

ra bb kc    = red to A, blue to B, black to C

numRed = 0
numBlu = 0
numBlk = 0

'''

red   = [['___', '___', 'CUT'],
         ['___', 'CUT', '___'],
         ['CUT', '___', '___'],
         ['CUT', '___', 'CUT'],
         ['___', 'CUT', '___'],
         ['CUT', '___', 'CUT'],
         ['CUT', 'CUT', 'CUT'],
         ['CUT', 'CUT', '___'],
         ['___', 'CUT', '___']]

blue  = [['___', 'CUT', '___'],
         ['CUT', '___', 'CUT'],
         ['___', 'CUT', '___'],
         ['CUT', '___', '___'],
         ['___', 'CUT', '___'],
         ['___', 'CUT', 'CUT'],
         ['___', '___', 'CUT'],
         ['CUT', '___', 'CUT'],
         ['CUT', '___', '___']]

black = [['CUT', 'CUT', 'CUT'],
         ['CUT', '___', 'CUT'],
         ['___', 'CUT', '___'],
         ['CUT', '___', 'CUT'],
         ['___', 'CUT', '___'],
         ['___', 'CUT', 'CUT'],
         ['CUT', 'CUT', '___'],
         ['___', '___', 'CUT'],
         ['___', '___', 'CUT']]

numRed   = 0
numBlue  = 0
numBlack = 0

toNum = {'a':0, 'b':1, 'c':2}

def translate(c):
    global numRed, numBlue, numBlack
    if len(c)!=2:
        print("  Invalid wire code!")
    else:
        if c[0]=='r':
            numRed += 1
            return red[numRed-1][toNum[c[1]]]
        elif c[0]=='b':
            numBlue += 1
            return blue[numBlue-1][toNum[c[1]]]
        elif c[0]=='k':
            numBlack += 1
            return black[numBlack-1][toNum[c[1]]]

def sequence_help():
    print("      <c><e> <c><e> <c><e>")
    print("      For each wire, enter the color code and endpoint.")
    print("        Red      r")
    print("        Blue     b")
    print("        Black    k")
    print("      Do not space for one wire, but put spaces between separate wires.")
    print("      Type 'q' to quit or 'reset' when restarting a new sequence module.")

def prompt_sequence():
    global numRed, numBlue, numBlack
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Wire Codes:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            sequence_help()
        elif user_input=="reset":
            numRed = 0
            numBlue = 0
            numBlack = 0
        else:
            wires = [translate(c) for c in user_input.split(' ')]
            print("  " + ' '.join(wires))
        print()
