#!/usr/bin/env python3
import sys

synonyms_tbl = {'inverted':  ('inverted', 'reverse', 'upside', 'down', 'upside-down'), \
                'backwards': ('backwards', 'reverse', 'inverted'), \
                'line':      ('line', 'stick', 'beard', 't', 'slash', 'bar', 'cross'), \
                'hook':      ('hook', 'curl', 'tail')
                'snake':     ('snake', 'dragon', 'worm', 'squiggly', 'funky')
                'dot':       ('dot', 'dots', 'point', 'period')
                'curly':     ('curly', 'cursive', 'fancy', 'script')
                '2':         ('2', 'two')
                '3':         ('3', 'three')
}

help_tbl = [
            (10, 'ae', 'a', 'e', 'Greek'),                                          \
            (11, 'y', 'lambda', 'inverted', 'line', 'Greek'),                       \
            (12, 'Y', 'psi', 'trident', 'pitchfork', 'Greek'),                      \
            (13, 'U', 'omega', 'horseshoe', 'Greek')                                \
            (24, 'W', 'butt', 'pumpkin', 'comma', 'Greek', 'omega'),                \
            (),                                                                     \
            (5,  'C.', 'C', 'dot', 'forwards', 'Greek', 'lunate', 'sigma'),         \
            (6,  '.)', 'C', 'dot', 'backwards', 'Greek', 'lunate', 'sigma'),        \
            (1,  'O', 'line', 'balloon', 'Greek', 'koppa'),                         \
            (20, 'Z', 'lightning', 'snake', 'zigzag', 'Greek', 'koppa'),            \
            (3,  'H', 'curly', 'Greek', 'kai'),                                     \
            (),                                                                     \
            (9,  'N', 'hook', 'hat', 'backwards', 'Cyrillic', 'I'),                 \
            (8,  'K', 'Cyrillic', 'zhje', 'backwards', 'double', 'hook'),           \
            (7,  'E', 'euro', 'backwards', '2', 'dot', 'Cyrillic'),                 \
            (0,  'A', 'at', 'mountain', 'line', 'Cyrillic', 'yus'),                 \
            (23, 'cat', 'spider', 'squid', 'line', 'triangle', 'Cyrillic', 'yus'),  \
            (),                                                                     \
            (2,  'o', 'curly', 'Cyrillic', 'hook'),                                 \
            (15, '6', 'flat', 'Cyrillic', 'be'),                                    \
            (14, 'b', 'line', 'bt', 'Cyrillic', 'yat'),                             \
            (26, '3', 'hook', 'Cyrillic', 'komi', 'dzje', )                         \
            (16, '3', 'antennae', 'hook', 'snake', 'Cyrillic', 'ksi'),              \
            (17, '=', 'not', 'equals', 'railroad', 'line', 'bars', 'Cyrillic'),     \
            (),                                                                     \
            (19, '?', 'question', 'mark', 'inverted'),                              \
            (21, '*', 'star', 'white', 'blank', 'empty', 'hollow', 'white'),        \
            (22, '**', '*', 'star', 'black', 'filled'),                             \
            (4,  'c', 'copyright', 'circle', 'ring'),                               \
            (18, 'P', 'backwards', 'pilcrow', 'paragraph'),                         \
            (25, ':)', 'smiley', 'face', 'tongue', 'Arabic', 'teh', '2', 'dot')]


def symbols_help():
    for i in range(26):
        print(' '.join(help_tbl[i][1:]) + '\t' + symbols_tbl[i])


def prompt_symbols():
    global serial_num
    global last_digit
    quit = False
    while not quit:
        user_input = input("> Color codes:\t").lower()
        if user_input=="help":
            symbols_help()
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

print("Symbols")
prompt_symbols()