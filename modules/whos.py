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

wordlist = {"ready"  : ["YES","OKAY","WHAT","MIDDLE","LEFT","PRESS","RIGHT","BLANK","READY","NO","FIRST","UHHH","NOTHING","WAIT"],
            "first"  : ["LEFT","OKAY","YES","MIDDLE","NO","RIGHT","NOTHING","UHHH","WAIT","READY","BLANK","WHAT","PRESS","FIRST"],
            "no"     : ["LEFT","OKAY","YES","MIDDLE","NO","RIGHT","NOTHING","UHHH","WAIT","READY","BLANK","WHAT","PRESS","FIRST"],
            "blank"  : ["WAIT","RIGHT","OKAY","MIDDLE","BLANK","PRESS","READY","NOTHING","NO","WHAT","LEFT","UHHH","YES","FIRST"],
            "nothing": ["UHHH","RIGHT","OKAY","MIDDLE","YES","BLANK","NO","PRESS","LEFT","WHAT","WAIT","FIRST","NOTHING","READY"],
            "yes"    : ["OKAY","RIGHT","UHHH","MIDDLE","FIRST","WHAT","PRESS","READY","NOTHING","YES","LEFT","BLANK","NO","WAIT"],
            "what"   : ["UHHH","WHAT","LEFT","NOTHING","READY","BLANK","MIDDLE","NO","OKAY","FIRST","WAIT","YES","PRESS","RIGHT"],
            "uhhh"   : ["READY","NOTHING","LEFT","WHAT","OKAY","YES","RIGHT","NO","PRESS","BLANK","UHHH","MIDDLE","WAIT","FIRST"],
            "left"   : ["RIGHT","LEFT","FIRST","NO","MIDDLE","YES","BLANK","WHAT","UHHH","WAIT","PRESS","READY","OKAY","NOTHING"],
            "right"  : ["YES","NOTHING","READY","PRESS","NO","WAIT","WHAT","RIGHT","MIDDLE","LEFT","UHHH","BLANK","OKAY","FIRST"],
            "middle" : ["BLANK","READY","OKAY","WHAT","NOTHING","PRESS","NO","WAIT","LEFT","MIDDLE","RIGHT","FIRST","UHHH","YES"],
            "okay"   : ["MIDDLE","NO","FIRST","YES","UHHH","NOTHING","WAIT","OKAY","LEFT","READY","BLANK","PRESS","WHAT","RIGHT"],
            "wait"   : ["UHHH","NO","BLANK","OKAY","YES","LEFT","FIRST","PRESS","WHAT","WAIT","NOTHING","READY","RIGHT","MIDDLE"],
            "press"  : ["RIGHT","MIDDLE","YES","READY","PRESS","OKAY","NOTHING","UHHH","BLANK","LEFT","FIRST","WHAT","NO","WAIT"],
            "you"    : ["SURE","YOU ARE","YOUR","YOU'RE","NEXT","UH HUH","UR","HOLD","WHAT?","YOU","UH UH","LIKE","DONE","U"],
            "you are": ["YOUR","NEXT","LIKE","UH HUH","WHAT?","DONE","UH UH","HOLD","YOU","U","YOU'RE","SURE","UR","YOU ARE"],
            "your"   : ["UH UH","YOU ARE","UH HUH","YOUR","NEXT","UR","SURE","U","YOU'RE","YOU","WHAT?","HOLD","LIKE","DONE"],
            "you're" : ["YOU","YOU'RE","UR","NEXT","UH UH","YOU ARE","U","YOUR","WHAT?","UH HUH","SURE","DONE","LIKE","HOLD"],
            "ur"     : ["DONE","U","UR","UH HUH","WHAT?","SURE","YOUR","HOLD","YOU'RE","LIKE","NEXT","UH UH","YOU ARE","YOU"],
            "u"      : ["UH HUH","SURE","NEXT","WHAT?","YOU'RE","UR","UH UH","DONE","U","YOU","LIKE","HOLD","YOU ARE","YOUR"],
            "uh huh" : ["UH HUH","YOUR","YOU ARE","YOU","DONE","HOLD","UH UH","NEXT","SURE","LIKE","YOU'RE","UR","U","WHAT?"],
            "uh uh"  : ["UR","U","YOU ARE","YOU'RE","NEXT","UH UH","DONE","YOU","UH HUH","LIKE","YOUR","SURE","HOLD","WHAT?"],
            "what?"  : ["YOU","HOLD","YOU'RE","YOUR","U","DONE","UH UH","LIKE","YOU ARE","UH HUH","UR","NEXT","WHAT?","SURE"],
            "done"   : ["SURE","UH HUH","NEXT","WHAT?","YOUR","UR","YOU'RE","HOLD","LIKE","YOU","U","YOU ARE","UH UH","DONE"],
            "next"   : ["WHAT?","UH HUH","UH UH","YOUR","HOLD","SURE","NEXT","LIKE","DONE","YOU ARE","UR","YOU'RE","U","YOU"],
            "hold"   : ["YOU ARE","U","DONE","UH UH","YOU","UR","SURE","WHAT?","YOU'RE","NEXT","HOLD","UH HUH","YOUR","LIKE"],
            "sure"   : ["YOU ARE","DONE","LIKE","YOU'RE","YOU","HOLD","UH HUH","UR","SURE","U","WHAT?","NEXT","YOUR","UH UH"],
            "like"   : ["YOU'RE","NEXT","U","UR","HOLD","DONE","UH UH","WHAT?","UH HUH","YOU","LIKE","SURE","YOU ARE","YOUR"]}

def wires_help():
    print("      Enter the header as-is. Then, enter the 6 words below in the following order:")
    print("        |  1  |  4  |")
    print("        |  2  |  5  |")
    print("        |  3  |  6  |")
    print("      Type 'q' to quit.")

def prompt_whos():
    pass
