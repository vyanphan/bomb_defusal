#!/usr/bin/env python3

syns_tbl = {'inverted':  {'inverted', 'reverse', 'upside', 'down', 'upside-down'}, \
            'backwards': {'backwards', 'backward', 'reverse', 'inverted'},         \
            'line':      {'line', 'stick', 'beard', 't', 'slash', 'bar', 'cross'}, \
            'hook':      {'hook', 'curl', 'tail', 'beard'},                        \
            'snake':     {'snake', 'dragon', 'worm', 'squiggly', 'funky'},         \
            'dot':       {'dot', 'dots', 'point', 'period'},                       \
            'curly':     {'curly', 'cursive', 'fancy', 'script'},                  \
            '2':         {'2', 'two'},                                             \
            '3':         {'3', 'three'}}

help_tbl = [
            ('ae' , 'a', 'e', 'greek'),                                         \
            ('y'  , 'lambda', 'inverted', 'line', 'greek'),                     \
            ('Y'  , 'y', 'psi', 'trident', 'pitchfork', 'greek'),               \
            ('U'  , 'omega', 'u', 'horseshoe', 'greek'),                        \
            ('W'  , 'w', 'butt', 'pumpkin', 'comma', 'greek'),                  \
            (),                                                                 \
            ('C.' , 'c', 'c.', 'dot', 'forwards', 'greek', 'lunate', 'sigma'),  \
            ('.)' , 'c', 'c.', 'dot', 'backwards', 'greek', 'lunate', 'sigma'), \
            ('O'  , 'o', 'line', 'balloon', 'tennis', 'greek', 'koppa'),        \
            ('Z'  , 'z', 'lightning', 'snake', 'zigzag', 'greek', 'koppa'),     \
            ('H'  , 'h', 'curly', 'greek', 'kai'),                              \
            (),                                                                 \
            ('N'  , 'n', 'hook', 'hat', 'backwards', 'cyrillic', 'I'),          \
            ('K'  , 'k', 'cyrillic', 'zhje', 'backwards', 'double', 'hook'),    \
            ('E'  , 'e', 'euro', 'backwards', '2', 'dot', 'cyrillic'),          \
            ('A'  , 'a', 'at', 'mountain', 'line', 'cyrillic', 'yus'),          \
            ('cat', 'kitty', 'spider', 'squid', 'triangle', 'cyrillic', 'yus'), \
            (),                                                                 \
            ('o'  , 'curly', 'cyrillic', 'hook'),                               \
            ('6'  , 'flat', 'cyrillic', 'be'),                                  \
            ('b'  , 'line', 'bt', 'cyrillic', 'yat'),                           \
            ('3'  , 'melted', 'hook', 'cyrillic', 'komi', 'dzje'),              \
            ('3(' , '3', 'antennae', 'hook', 'snake', 'cyrillic', 'ksi'),       \
            ('='  , 'not', 'equals', 'railroad', 'line', 'bars', 'cyrillic'),   \
            (),                                                                 \
            ('?'  , 'question', 'mark', 'inverted'),                            \
            ('*'  , 'star', 'white', 'blank', 'empty', 'hollow', 'white'),      \
            ('**' , '*', 'star', 'black', 'filled'),                            \
            ('c'  , 'copyright', 'circle', 'ring'),                             \
            ('P'  , 'p', 'backwards', 'pilcrow', 'paragraph'),                  \
            (':)' , 'smiley', 'face', 'tongue', 'arabic', 'teh', '2', 'dot')]

symb_tbl = [['O', 'A' , 'y' , 'Z'  , 'cat', 'H' , '.)'], \
            ['E', 'O' , '.)', 'o'  , '*'  , 'H' , '?' ], \
            ['c', 'W' , 'o' , 'K'  , '3'  , 'y' , '*' ], \
            ['6', 'P' , 'b' , 'cat', 'K'  , '?' , ':)'], \
            ['Y', ':)', 'b' , 'C.' , 'P'  , '3(', '**'], \
            ['6', 'E' , '=' , 'ae' , 'Y'  , 'N' , 'U' ]]

def parse_input(user_input):
    symbols = user_input.split(' ')
    if len(symbols)<1:
        return None
    elif symbols[0].lower()=='help':
        if len(symbols)==1 :
            print("    Enter symbol codes separated by spaces (in any order).")
            print("    Type \"help all\" to see the full list of symbol codes.")
            print("    Type \"help <item>\" to find specific terms; separate tags with spaces.")
        elif symbols[1].lower()=='all':
            symbols_help(None)
        else:
            symbols_help(set([s.lower() for s in symbols[1:]]))
    else:
        return symbols

def symbols_help(search):
    if search==None:
        print("      Code\tDescription of Symbol")
        print("      ────\t───────────────────────────────────────────")
        for symbol in help_tbl:
            if symbol==():
                print()
            else:
                print("      " + symbol[0] + '\t\t' + ' '.join(symbol))
    else:
        result = {}
        print("      Code\tDescription of Symbol")
        print("      ────\t───────────────────────────────────────────")
        for symbol in help_tbl:
            for tag in symbol:
                if tag in search or tag in syns_tbl and len(search&syns_tbl[tag])>0:
                    if symbol in result:
                        result[symbol] += 1
                    else:
                        result[symbol] = 1
        if len(result)>0:
            maxMatches = max(result.values())
            for symbol in [s for s in result if result[s]==maxMatches]:
                print("      " + symbol[0] + '\t\t' + ' '.join(symbol))

def symbols_solve(symbols):
    for slist in symb_tbl:
        if sum([1 for s in symbols if s in slist])==4:
            return [sl for sl in slist if sl in symbols]
    return -1

def prompt_symbols():
    global serial_num
    global last_digit
    quit = False
    while not quit:
        user_input = input("  > Symbols:\t")
        symbols = parse_input(user_input)
        if user_input=="q":
            quit = True
        elif symbols==None or len(symbols)!=4:
            pass
        else:
            ans = symbols_solve(symbols)
            if ans==-1:
                print("  Incorrect symbol code.")
            else:
                print("  " + ' '.join(ans))
        print()
