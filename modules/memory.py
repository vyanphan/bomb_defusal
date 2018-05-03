#!/usr/bin/env python3

'''
<display><b><b><b><b>
> Stage 1: 51234
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


def stage1_solve():
    pass

def stage2_solve():
    pass

def stage3_solve():
    pass

def stage4_solve():
    pass

def stage5_solve():
    pass

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
        elif user_input=="reset all":
            pass
        else:
            
            


            stage = min(5, stage+1)
        
        if stage==5:
            # reset all
            print()
