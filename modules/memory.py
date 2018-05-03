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
        return buttons[2], 2
    elif buttons[0]=='3':
        return buttons[3], 3
    elif buttons[0]=='4':
        return buttons[4], 4

def stage2_solve(buttons):
    if buttons[0]=='1':
        return '4', buttons.index('4')
    elif buttons[0]=='2' or buttons[0]=='4':
        return buttons[stages[1][2]], stages[1][2]
    elif buttons[0]=='3':
        return buttons[1], 1

def stage3_solve(buttons):
    if buttons[0]=='1':
        return stages[2][1], buttons.index(stages[2][1])
    elif buttons[0]=='2':
        return stages[1][1], buttons.index(stages[1][1])
    elif buttons[0]=='3':
        return buttons[3], 3
    elif buttons[0]=='4':
        return '4', buttons.index('4')

def stage4_solve(buttons):
    if buttons[0]=='1':
        return buttons[stages[1][2]], stages[1][2]
    elif buttons[0]=='2':
        return buttons[1], 1
    elif buttons[0]=='3' or buttons[0]=='4':
        return buttons[stages[2][2]], stages[2][2]

def stage5_solve(buttons):
    if buttons[0]=='1':
        return stages[1][1], buttons.index(stages[1][1])
    elif buttons[0]=='2':
        return stages[2][1], buttons.index(stages[2][1])
    elif buttons[0]=='3':
        return stages[4][1], buttons.index(stages[4][1])
    elif buttons[0]=='4':
        return stages[3][1], buttons.index(stages[3][1])

def memory_help(buttons):
    pass

stages = {1: [[], 0, -1, stage1_solve],
          2: [[], 0, -1, stage2_solve],
          3: [[], 0, -1, stage3_solve],
          4: [[], 0, -1, stage4_solve],
          5: [[], 0, -1, stage5_solve]}

def prompt_memory():
    quit = False
    stage = 1
    while not quit:
        if stage==1:
            user_input = input("  > {0:16}".format("Stage "+ str(stage) +":")).strip().lower()
        elif stage==6:
            user_input = input("    {0:16}".format("End:")).strip().lower()
        else:
            user_input = input("    {0:16}".format("Stage "+ str(stage) +":")).strip().lower()

        if user_input=="q":
            quit = True
        elif user_input=="help":
            memory_help()
        elif user_input=="reset":
            stage = max(1, stage-1)
            if stage==1:
                print()
        elif user_input=="reset all":
            stage = 6
        elif stage==6:
            stage += 1

        elif stage>0 and stage<6:
            s = stages[stage]
            s[0] = [c for c in user_input]
            if len(s[0])!=5:
                print("  Invalid button input!")
            else:
                s[1], s[2] = s[3](s[0])
                print("      " + s[1])
                stage += 1
        
        if stage>6:
            stage = 1
            print()
