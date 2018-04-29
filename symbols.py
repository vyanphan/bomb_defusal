#!/usr/bin/env python3
import sys

synonyms_tbl = {'inverted':  ('inverted', 'reverse', 'upside', 'down', 'upside-down'), \
                'backwards': ('backwards', 'reverse', 'inverted'),                     \
                'line':      ('line', 'stick', 'beard', 't', 'slash', 'bar', 'cross'), \
                'hook':      ('hook', 'curl', 'tail'),                                 \
                'snake':     ('snake', 'dragon', 'worm', 'squiggly', 'funky'),         \
                'dot':       ('dot', 'dots', 'point', 'period'),                       \
                'curly':     ('curly', 'cursive', 'fancy', 'script'),                  \
                '2':         ('2', 'two'),                                             \
                '3':         ('3', 'three')}

help_tbl = [
            ('ae' , 'a', 'e', 'Greek'),                                         \
            ('y'  , 'lambda', 'inverted', 'line', 'Greek'),                     \
            ('Y'  , 'psi', 'trident', 'pitchfork', 'Greek'),                    \
            ('U'  , 'omega', 'horseshoe', 'Greek'),                             \
            ('W'  , 'butt', 'pumpkin', 'comma', 'Greek', 'omega'),              \
            (),                                                                 \
            ('C.' , 'C', 'dot', 'forwards', 'Greek', 'lunate', 'sigma'),        \
            ('.)' , 'C', 'dot', 'backwards', 'Greek', 'lunate', 'sigma'),       \
            ('O'  , 'line', 'balloon', 'Greek', 'koppa'),                       \
            ('Z'  , 'lightning', 'snake', 'zigzag', 'Greek', 'koppa'),          \
            ('H'  , 'curly', 'Greek', 'kai'),                                   \
            (),                                                                 \
            ('N'  , 'hook', 'hat', 'backwards', 'Cyrillic', 'I'),               \
            ('K'  , 'Cyrillic', 'zhje', 'backwards', 'double', 'hook'),         \
            ('E'  , 'euro', 'backwards', '2', 'dot', 'Cyrillic'),               \
            ('A'  , 'at', 'mountain', 'line', 'Cyrillic', 'yus'),               \
            ('cat', 'spider', 'squid', 'line', 'triangle', 'Cyrillic', 'yus'),  \
            (),                                                                 \
            ('o'  , 'curly', 'Cyrillic', 'hook'),                               \
            ('6'  , 'flat', 'Cyrillic', 'be'),                                  \
            ('b'  , 'line', 'bt', 'Cyrillic', 'yat'),                           \
            ('3'  , 'hook', 'Cyrillic', 'komi', 'dzje'),                        \
            ('3'  , 'antennae', 'hook', 'snake', 'Cyrillic', 'ksi'),            \
            ('='  , 'not', 'equals', 'railroad', 'line', 'bars', 'Cyrillic'),   \
            (),                                                                 \
            ('?'  , 'question', 'mark', 'inverted'),                            \
            ('*'  , 'star', 'white', 'blank', 'empty', 'hollow', 'white'),      \
            ('**' , '*', 'star', 'black', 'filled'),                            \
            ('c'  , 'copyright', 'circle', 'ring'),                             \
            ('P'  , 'backwards', 'pilcrow', 'paragraph'),                       \
            (':)' , 'smiley', 'face', 'tongue', 'Arabic', 'teh', '2', 'dot')]

def parse_input(user_input):
    symbols = user_input.lower().split(' ')
    if len(symbols)<1:
        return None
    elif symbols[0]=='help':
        symbols_help(symbols)
    else:
        return symbols

def symbols_help(search):
    if len(search)==1:
        print("  Type \"help <search tag>\" to find a specific term.")
        print("  Separate multiple tags with spaces.")
        print("    Code\tDescription of Symbol")
        print("    ────\t───────────────────────────────────────────")
        for symbol in help_tbl:
            if symbol==():
                print()
            else:
                print("    " + symbol[0] + '\t\t' + ' '.join(symbol))



def prompt_symbols():
    global serial_num
    global last_digit
    quit = False
    while not quit:
        user_input = input("> Symbols:\t").lower()
        symbols = parse_input(user_input)
        if user_input=="q":
            quit = True
        elif symbols==None or len(symbols)!=4:
            pass
        else:
            pass
        print()

print("Symbols")
prompt_symbols()