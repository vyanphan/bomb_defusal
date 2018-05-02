#!/usr/bin/env python3
from modules import *

mods_list = ["Wires", "Button", "Keypads", "Simon Says", "Who's on First", "Memory", "Morse Code",
             "Complicated Wires", "Wire Sequences", "Mazes", "Passwords", "Knobs"]

syns_list = [["wire", "wires", "simple wire", "simple wires", "easy wire", "easy wires", "easy"],
             ["button", "buttons"],
             ["keypad", "keypads", "symbol", "symbols"],
             ["simon", "simon says"],
             ["who's on first", "who's on 1st", "whos on first", "whos on 1st", "whos", "1st"],
             ["memory", "memory wires", "memory wire"],
             ["morse code", "morse"],
             ["complicated wires", "complicated wire", "complicated", "hard wires", "hard"],
             ["wire sequences", "sequence wires", "sequence wire", "sequence"],
             ["maze", "mazes"],
             ["password", "passwords", "letters"],
             ["knob", "knobs", "needy"]]

cmds_list = [wire.prompt_wire,
             button.prompt_button,
             keypad.prompt_keypad,
             simon.prompt_simon]

def help_main():
    print("  Type the name of the module to get started.")
    print("  Commands for the main prompt:")
    print("    {0:10}{1}".format("q"       , "Quits the whole program."))
    print("    {0:10}{1}".format("help"    , "Displays the general help menu."))
    print("    {0:10}{1}".format("help all", "Lists all possible modules."))
    print("    {0:10}{1}".format("reset"   , "Clears all saved information."))
    print("  Commands for specific modules:")
    print("    {0:10}{1}".format("q"       , "Quits the module and returns to the main menu."))
    print("    {0:10}{1}".format("help"    , "Displays general help for that module."))
    print("    {0:10}{1}".format("reset"   , "Clears saved information for that module only."))
    print("  Saved information refers to items applying to the entire bomb, e.g.")
    print("    number of batteries")
    print("    serial number")
    print("    number of strikes")

def help_all():
    print("  {0:20}{1}".format("Module", "Synonyms"))
    print("  " + "─" * 87)
    for i in range(len(mods_list)):
        print("  {0:20}{1}".format(mods_list[i], ", ".join(syns_list[i])))

commands = {"help"     : help_main,
            "help all" : help_all,
            "reset"    : globvars.reset_all}
for i in range(len(cmds_list)):
    for term in syns_list[i]:
        commands[term] = cmds_list[i]

def prompt_main():
    quit = False
    while not quit:
        user_input = input("[MODULE] ").strip().lower()
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
