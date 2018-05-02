#!/usr/bin/env python3

headers = {"yes"     :1,
           "first"   :3,
           "display" :5,
           "okay"    :3,
           "says"    :5,
           "nothing" :1,
           ""        :2,
           "blank"   :4,
           "no"      :5,
           "led"     :1,
           "lead"    :5,
           "read"    :4,
           "red"     :4,
           "reed"    :2,
           "leed"    :2,
           "hold on" :5,
           "you"     :4,
           "you are" :5,
           "your"    :4,
           "you're"  :4,
           "ur"      :0,
           "there"   :5,
           "they're" :2,
           "their"   :4,
           "they are":1,
           "see"     :5,
           "c"       :3,
           "cee"     :5}

wordlist = {"ready"  : ["yes","okay","what","middle","left","press","right","blank","ready","no","first","uhhh","nothing","wait"],
            "first"  : ["left","okay","yes","middle","no","right","nothing","uhhh","wait","ready","blank","what","press","first"],
            "no"     : ["left","okay","yes","middle","no","right","nothing","uhhh","wait","ready","blank","what","press","first"],
            "blank"  : ["wait","right","okay","middle","blank","press","ready","nothing","no","what","left","uhhh","yes","first"],
            "nothing": ["uhhh","right","okay","middle","yes","blank","no","press","left","what","wait","first","nothing","ready"],
            "yes"    : ["okay","right","uhhh","middle","first","what","press","ready","nothing","yes","left","blank","no","wait"],
            "what"   : ["uhhh","what","left","nothing","ready","blank","middle","no","okay","first","wait","yes","press","right"],
            "uhhh"   : ["ready","nothing","left","what","okay","yes","right","no","press","blank","uhhh","middle","wait","first"],
            "left"   : ["right","left","first","no","middle","yes","blank","what","uhhh","wait","press","ready","okay","nothing"],
            "right"  : ["yes","nothing","ready","press","no","wait","what","right","middle","left","uhhh","blank","okay","first"],
            "middle" : ["blank","ready","okay","what","nothing","press","no","wait","left","middle","right","first","uhhh","yes"],
            "okay"   : ["middle","no","first","yes","uhhh","nothing","wait","okay","left","ready","blank","press","what","right"],
            "wait"   : ["uhhh","no","blank","okay","yes","left","first","press","what","wait","nothing","ready","right","middle"],
            "press"  : ["right","middle","yes","ready","press","okay","nothing","uhhh","blank","left","first","what","no","wait"],
            "you"    : ["sure","you are","your","you're","next","uh huh","ur","hold","what?","you","uh uh","like","done","u"],
            "you are": ["your","next","like","uh huh","what?","done","uh uh","hold","you","u","you're","sure","ur","you are"],
            "your"   : ["uh uh","you are","uh huh","your","next","ur","sure","u","you're","you","what?","hold","like","done"],
            "you're" : ["you","you're","ur","next","uh uh","you are","u","your","what?","uh huh","sure","done","like","hold"],
            "ur"     : ["done","u","ur","uh huh","what?","sure","your","hold","you're","like","next","uh uh","you are","you"],
            "u"      : ["uh huh","sure","next","what?","you're","ur","uh uh","done","u","you","like","hold","you are","your"],
            "uh huh" : ["uh huh","your","you are","you","done","hold","uh uh","next","sure","like","you're","ur","u","what?"],
            "uh uh"  : ["ur","u","you are","you're","next","uh uh","done","you","uh huh","like","your","sure","hold","what?"],
            "what?"  : ["you","hold","you're","your","u","done","uh uh","like","you are","uh huh","ur","next","what?","sure"],
            "done"   : ["sure","uh huh","next","what?","your","ur","you're","hold","like","you","u","you are","uh uh","done"],
            "next"   : ["what?","uh huh","uh uh","your","hold","sure","next","like","done","you are","ur","you're","u","you"],
            "hold"   : ["you are","u","done","uh uh","you","ur","sure","what?","you're","next","hold","uh huh","your","like"],
            "sure"   : ["you are","done","like","you're","you","hold","uh huh","ur","sure","u","what?","next","your","uh uh"],
            "like"   : ["you're","next","u","ur","hold","done","uh uh","what?","uh huh","you","like","sure","you are","your"]}

def whos_help():
    print("      First, enter the display as-is.")
    print("      Then, enter the 6 words as-is, separated by commas (no spaces), in this order:")
    print("        |  1  |  4  |")
    print("        |  2  |  5  |")
    print("        |  3  |  6  |")
    print("      Type 'q' to quit.")

def solve_whos(key, buttons):
    try:
        words = wordlist[key]
        for w in words:
            if w in buttons:
                print("  " + w)
                break
    except:
        print("  Invalid button entry!")


def prompt_whos():
    quit = False
    while not quit:
        user_input = input("  > {0:16}".format("Display:")).strip().lower()
        if user_input=="q":
            quit = True
        elif user_input=="help":
            whos_help()
        else:
            try:
                buttons = input("  > {0:16}".format("Buttons:")).strip().lower().split(",")
                key = buttons[headers[user_input]]
                solve_whos(key, buttons)
            except:
                print("  Invalid display entry!")
        print()
