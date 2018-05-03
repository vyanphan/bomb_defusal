#!/usr/bin/env python3

'''
<display> <b><b><b><b>
> Stage 1: 5 1234
    0   = display1
    []  = buttons1
    i   = prespos1
    n   = preslab1
  Stage 2:
  Stage 3:
  Stage 4:
  Stage 5:

Reset clears current stage.
Reset all clears everything and returns to stage 1.
Will automatically reset all at stage 5.
'''


def memory_help():
    pass

def prompt_memory():
    quit = False
    stage = 1
    while not quit:
        user_input = input("  > {0:16}".format("Stage "+ str(stage) +":")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            memory_help()
        elif user_input=="reset":
            stage = max(1, stage-1)
        else:
            pass
        print()
