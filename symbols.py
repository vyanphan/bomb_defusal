#!/usr/bin/env python3
import sys

help_tbl = [(1,  'O', 'line', 'balloon', 'Greek', 'koppa'),                              \
            (0,  'A', 'at', 't', 'mountain', 'line', 'Cyrillic', 'yus'),                  \
            (11, 'lambda', 'y', 'upside', 'down', 'reverse', 'inverted', 'line', 'slash', 'Greek'),                        \
            (20, 'lightning', 'bolt', 'squiggly', 'zigzag', 'Greek', 'koppa'),                       \
            (23, 'cat', 'spider', 'squid', 'knife', 'bar', 'line', 'triangle', 'Cyrillic', 'yus'),                    \
            (3,  'Greek', 'kai', 'curly', 'cursive', 'fancy', 'script', 'H'),                            \
            (6,  'Greek', 'lunate', 'sigma', 'backwards', 'reverse', 'inverted', 'C', 'dot'),                  \
            
            (7,  'E', 'euro', '2', 'two', 'dot', 'dots', 'backwards', 'reverse', 'inverted', 'Cyrillic'),            \
            (2,  'Cyrillic', 'curly', 'cursive', 'fancy', 'script', 'o', 'hook'),                            \
            (21, 'blank', 'empty', 'hollow', 'white', 'star'),                         \
            (19, '?', 'question', 'mark', 'upside', 'down', 'reverse', 'inverted'),             \
            
            (4,  'copyright', 'circle', 'c', 'symbol'),                            \
            (24, 'W', 'butt', 'pumpkin', 'comma', 'Greek', 'omega'),                                \
            (8,  'K', 'Cyrillic', 'zhje', 'backwards', 'reverse', 'inverted', 'double', 'hook'),            \
            (26, '3', 'hook', 'Cyrillic', 'komi', 'dzje', )
            
            (15, 'Cyrllic', 'be', 'flat', '6'),                                      \
            (18, 'pilcrow', 'paragraph', 'symbol', 'reverse', 'inverted', 'backwards', 'P'),             \
            (14, 'Cyrillic', 'yat', 'b', 'cross', 't', 'bt'),                        \
            (25, 'Arabic', 'teh', 'ring', 'smiley', 'face', 'tongue')
            
            (12, 'Greek', 'psi', 'trident', 'pitchfork'),                                    \
            (5,  'Greek', 'lunate', 'sigma', 'forwards', 'C', 'dot'),                   \
            (16, 'Cyrillic', 'ksi', 'snake', 'funky', '3', 'antennae', 'hook', 'tail', 'dragon'),                               \
            (22, 'black', 'filled', 'star'),                                  \

            (17, 'Cyrillic', 'thousands', 'not', 'equals', 'railroad', 'track', 'bars'),                \
            (10, 'Greek', 'ae'),                                    \
            (9,  'Cyrillic', 'I', 'backwards', 'reverse', 'inverted', 'N', 'tail', 'hat'),   \
            (13, 'Greek', 'omega'),                                          \


symbols_tbl = ['A', 'O', 'o', 'H', 'c', 'C.', '.)', 'E..', 'K', 'N', 'ae', 'L', 'Y', \
               'U', 'b', '6', '3', '=', 'P', '?', 'Z', '*', '**', 'cat', 'W', ':)']

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