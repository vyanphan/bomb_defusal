#!/usr/bin/env python3
from modules import *

mods_list = ["Wires", "Button", "Keypads", "Simon Says", "Who's on First", "Memory", "Morse Code",
             "Complicated Wires", "Wire Sequences", "Mazes", "Passwords", "Knobs"]

syns_list = [["wire", "wires", "simple wire"]
]

def help_main():
    print("  Type 'q' within a module to quit that single module.")
    print("  Type 'q' in the main prompt to exit the whole program.")
    print("  Type 'help all' to view a list of the possible modules.")
    print("  Type 'reset' within a module to clear saved information for that specific module.")
    print("  Type 'reset' in the main prompt to reset all saved information.")

def help_all():
    for m in mods_list:
        print("  " + m)

commands = {"help"              : help_main,
            "help all"          : help_all,
            "reset"             : global_vars.reset_all,
            "wire"              : simple_wires.prompt_simple_wires,
            "wires"             : simple_wires.prompt_simple_wires,
            "simple wire"       : simple_wires.prompt_simple_wires,
            "simple wires"      : simple_wires.prompt_simple_wires,
            "simple"            : simple_wires.prompt_simple_wires,
            "easy wire"         : simple_wires.prompt_simple_wires,
            "easy wires"        : simple_wires.prompt_simple_wires,
            "easy"              : simple_wires.prompt_simple_wires,
            "button"            : button.prompt_button,
            "buttons"           : button.prompt_button,
            "keypad"            : symbols.prompt_symbols,
            "keypads"           : symbols.prompt_symbols,
            "symbol"            : symbols.prompt_symbols,
            "symbols"           : symbols.prompt_symbols
}



def prompt_main():
    quit = False
    while not quit:
        user_input = input("[MODULE] ").lower()
        print()
        if user_input=="q":
            quit = True
        else:
            commands[user_input]()
        # elif user_input in {"keypad", "keypads", "symbol", "symbols"}:
        #     symbols.prompt_symbols()


        print()

prompt_main()