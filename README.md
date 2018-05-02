Keep Talking and Nobody Explodes
=================================

## About

Keep Talking and Nobody Explodes is a logic-based game where one has to defuse a bomb by solving
the various puzzles on each of its modules. It is meant to be a multiplayer game where the one
person defusing the bomb is unable to see the manual, while the person with the manual is unable
to see the bomb.

More information about the game can be found [here](http://www.keeptalkinggame.com/).

The bomb defusal manual can be found [here](http://www.bombmanual.com/manual/1/html/index.html).
A pdf version of the manual is also in this repository.

This is an attempt to build a program that can solve the bombs perfectly each time based on the
information in the manual. It is meant to be an exercise in logic, not a replacement for actual
friends. (Seriously. It's not fun if it's just a bot.)

On the other hand, if you want to play with a friend but the friend is too lazy to learn how to
read the manual as they are supposed to, just hand them this bot and they can enter the inputs and
read aloud the outputs for you. Or just use the other bot that someone on YouTube made; it's voice
activated and probably way better than this one.


## Instructions

### Installation
- [Python 3](https://www.python.org/downloads/) is required. Install that first if you do not
  already have it.
- Clone this repository and use your preferred terminal to navigate to the location of the folder.
- Run `python3 main.py` to start the program.

### General
- When prompted, type the name of the module.
- To quit a module, or the entire program, type `q`.
- For general help, type `help`. To see all possible modules, type `help all`.
- To clear information already entered into a module, type `reset`.
- Most inputs are not case-sensitive, but make sure to use the formats as described below.

### On the Subject of Wires
- When the prompt appears, enter the color codes of the wires in (no spaces).
    ```
    Simple Wires
    > Color codes:  rwyr
      Serial#:      d7089c2
    2ND    
    ```
- Type `help` to see the color codes for each wire.
    | Color  | Code |
    |--------|------|
    | Blue   | B    |
    | Red    | R    |
    | Yellow | Y    |
    | Black  | K    |
    | White  | W    |
- If the prompt asks `Serial#` simply enter the serial number as shown on the bomb.
- Type `q` to quit the module or `reset` to clear `Serial#` if you entered it wrong by accident.

### On the Subject of The Button
- When the prompt appears, enter the color code and the button label as-is, with one space in
  between them.
    ```
    > Color Label:  r abort
      #Batteries:   3
      Indicator:    frk
    PRESS AND IMMEDIATELY RELEASE
    ```
- Type `help` to see the color codes for the button. Enter the button label as-is.
    | Color  | Code |
    |--------|------|
    | Blue   | B    |
    | Red    | R    |
    | Yellow | Y    |
    | Black  | K    |
    | White  | W    |
- If the prompt asks `#Batteries` enter the number of batteries around the bomb. If the prompt
  asks `Indicator` enter the label by the lit indicator (e.g. `CAR`, `FRK`).
- Type `q` to quit. Type `reset` to clear `#Batteries` and `Indicator` if you entered either wrong.

### On the Subject of Keypads
- When the prompt appears, enter the symbol codes of the buttons separated by spaces.
    ```
    > Symbols:      * .) O ?
    O .) * ?
    ```
- Type `help all` to see all the symbol codes. On the right will be a description of the symbol,
  and on the left will be the symbol code you should enter.
- Type `help <item>` to search for a specific term; separate multiple descriptors with spaces.
    ```
    > Symbols:    help c
        Code  Description of Symbol
        ──────────────────────────────────────────────────
        C.    C. c c. dot forwards greek lunate sigma
        .)    .) c c. dot backwards greek lunate sigma
        c     c copyright circle ring

    > Symbols:    help backwards c with dot
        Code  Description of Symbol
        ──────────────────────────────────────────────────
        .)    .) c c. dot backwards greek lunate sigma
    ```
- Type `q` to quit.
