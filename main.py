#!/usr/bin/env python3
from modules import *

mods_list = ["Wires", "Button", "Keypads", "Simon Says", "Who's on First", "Memory", "Morse Code",
             "Complicated Wires", "Wire Sequences", "Mazes", "Passwords", "Knobs"]

syns_list = [["wire", "wires", "simple wire", "simple wires", "easy wire", "easy wires", "easy"],
             ["button", "buttons"],
             ["keypad", "keypads", "symbol", "symbols"],
             ["simon", "simon says"],
             ["who's on first", "who's on 1st", "whos on first", "whos on 1st", "who", "whos", "first", "1st"],
             ["memory", "memory wires", "memory wire"],
             ["morse code", "morse"],
             ["complicated wires", "complicated wire", "complicated", "hard wires", "hard wire", "hard"],
             ["wire sequences", "sequence wires", "sequence wire", "sequence"],
             ["maze", "mazes"],
             ["password", "passwords", "letters"],
             ["knob", "knobs", "needy"]]

cmds_list = [simple_wires.prompt_simple_wires,
             button.prompt_button,
             symbols.prompt_symbols]

def help_main():
    print("  Type 'q' within a module to quit that single module.")
    print("  Type 'q' in the main prompt to exit the whole program.")
    print("  Type 'help all' to view a list of the possible modules.")
    print("  Type 'reset' within a module to clear saved information for that specific module.")
    print("  Type 'reset' in the main prompt to reset all saved information.")

def help_all():
    for i in range(len(mods_list)):
        for s in syns_list[i]:
            print("".format(mods_list[i], s))

commands = {"help"     : help_main,
            "help all" : help_all,
            "reset"    : global_vars.reset_all}
for i in range(len(cmds_list)):
    for term in syns_list[i]:
        commands[term] = cmds_list[i]

def prompt_main():
    quit = False
    while not quit:
        user_input = input("[MODULE] ").lower()
        print()
        if user_input=="q":
            quit = True
        else:
            try:
                commands[user_input]()
            except BaseException:
                print("Module does not exist.")
        print()

prompt_main()
