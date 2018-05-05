#!/usr/bin/env python3

'''
colors:     r   b   k

<c><pos> <c><pos> ...

ra bb kc    = red to A, blue to B, black to C

numRed = 0
numBlu = 0
numBlk = 0

'''

red   = [[0, 0, 1],
         [0, 1, 0],
         [1, 0, 0],
         [1, 0, 1],
         [0, 1, 0],
         [1, 0, 1],
         [1, 1, 1],
         [1, 1, 0],
         [0, 1, 0]]

blue  = [[0, 1, 0],
         [1, 0, 1],
         [0, 1, 0],
         [1, 0, 0],
         [0, 1, 0],
         [0, 1, 1],
         [0, 0, 1],
         [1, 0, 1],
         [1, 0, 0]]

black = [[1, 1, 1],
         [1, 0, 1],
         [0, 1, 0],
         [1, 0, 1],
         [0, 1, 0],
         [0, 1, 1],
         [1, 1, 0],
         [0, 0, 1],
         [0, 0, 1]]

numRed   = 0
numBlue  = 0
numBlack = 0

toNum = {'a':0, 'b':1, 'c':2}

def translate(c):
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
    pass

def prompt_sequence():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Wire Codes:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            sequence_help()
        else:
            wires = [translate(c) for c in user_input.split(' ')]
            print("  " + ' '.join(wires))
        print()
