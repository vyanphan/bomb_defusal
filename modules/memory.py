#!/usr/bin/env python3

'''
<display><b><b><b><b>
> Stage 1: 41234
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


def stage1_solve(buttons):
    if buttons[0]=='1' or buttons[0]=='2':
        return buttons[2]
    elif buttons[0]=='3':
        return buttons[3]
    elif buttons[0]=='4':
        return buttons[4]

def stage2_solve(buttons):
    pass

def stage3_solve(buttons):
    pass

def stage4_solve(buttons):
    pass

def stage5_solve(buttons1):
    pass

def memory_help(buttons):
    pass

stages = {1: stage1_solve,
          2: stage2_solve,
          3: stage3_solve,
          4: stage4_solve,
          5: stage5_solve}

def prompt_memory():
    quit = False
    stage = 1
    while not quit:
        if stage==1:
            user_input = input("  > {0:16}".format("Stage "+ str(stage) +":")).strip().lower()
        else:
            user_input = input("    {0:16}".format("Stage "+ str(stage) +":")).strip().lower()

        if user_input=="q":
            quit = True
        elif user_input=="help":
            memory_help()
        elif user_input=="reset":
            stage = max(1, stage-1)
        elif user_input=="reset all":
            stage = 6
        else:
            buttons = [c for c in user_input]
            if len(buttons)!=5:
                print("  Invalid button input!")
            else:
                stages[stage](buttons)
                stage += 1
        
        if stage>5:
            stage = 1
            print()
