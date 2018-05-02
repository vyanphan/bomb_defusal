Keep Talking and Nobody Explodes
=================================


## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Instructions](#instructions)
    - [General](#general)
    - [On the Subject of Wires](#on-the-subject-of-wires)
    - [On the Subject of The Button](#on-the-subject-of-the-button)
    - [On the Subject of Keypads](#on-the-subject-of-keypads)
    - [On the Subject of Simon Says](#on-the-subject-of-simon-says)
    - [On the Subject of Who's on First](#on-the-subject-of-whos-on-first)
    - [On the Subject of Memory](#on-the-subject-of-memory)
    - [On the Subject of Morse Code](#on-the-subject-of-morse-code)
    - [On the Subject of Complicated Wires](#on-the-subject-of-complicated-wires)
    - [On the Subject of Wire Sequences](#on-the-subject-of-wire-sequences)
    - [On the Subject of Mazes](#on-the-subject-of-mazes)
    - [On the Subject of Passwords](#on-the-subject-of-passwords)
    - [On the Subject of Knobs](#on-the-subject-of-knobs)

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


## Installation
- [Python 3](https://www.python.org/downloads/) is required. Install that first if you do not
  already have it.
- Clone this repository and use your preferred terminal to navigate to the location of the folder.
- Run `python3 main.py` to start the program.


## Instructions

### General
- When prompted, type the name of the module.
    ```
    [MODULE] wire

      > Color Codes:    rwyr
        Serial#:        abc7
      LAST RED

      > Color Codes:    q
    ```
- Commands for the main prompt

    | Command    | Action                       |
    |------------|------------------------------|
    | `q`        | Quits the whole program.     |
    | `help`     | Displays general help.       |
    | `help all` | Lists all possible modules.  |
    | `reset`    | Clears all saved information.|
- Commands for specific modules 

    | Command    | Action                                        |
    |------------|-----------------------------------------------|
    | `q`        | Quits the module and returns to the main menu.|
    | `help`     | Displays general help for that module.        |
    | `reset`    | Clears saved information for that module only.|
- "Saved information" refers to items applying to the entire bomb, e.g.
    - number of batteries
    - serial number
    - number of strikes

### On the Subject of Wires
- When the prompt appears, enter the color codes of the wires without spaces.
    ```
    Simple Wires
    > Color codes:  rwyr
      Serial#:      d7089c2
    2ND    
    ```
- Type `help` to see the color codes for each wire.

    | Color  | Code |
    |--------|------|
    | Red    | R    |
    | Blue   | B    |
    | Yellow | Y    |
    | White  | W    |
    | Black  | K    |
- If the prompt asks `Serial#` simply enter the serial number as shown on the bomb.
- Type `q` to quit to main menu. Type `reset` to clear `Serial#` if you entered it wrong.

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

    | Color           | Code |
    |-----------------|------|
    | Red             | R    |
    | Blue            | B    |
    | Yellow          | Y    |
    | White           | W    |
    | Any other color | X    |
- If the prompt asks `#Batteries` enter the number of batteries around the bomb.
- If the prompt asks `Indicator` enter all lit indicators (e.g. `CAR`, `FRK`), separated by spaces.
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

### On the Subject of Simon Says
- When the prompt appears, enter the color codes of the flashing lights without spaces.
    ```
    > Color Codes:    rgby
    b y r g
    ```
- Type `help` to see the color codes for each button.

    | Color  | Code |
    |--------|------|
    | Red    | R    |
    | Blue   | B    |
    | Green  | G    |
    | Yellow | Y    |
- If the prompt asks `Serial#` simply enter the serial number as shown on the bomb.
- Type `set <i>` to set a new number of `strikes`. For example, type `set 0` to clear `strikes`.
- Type `q` to quit. Type `reset` to clear `Serial#` ONLY.

### On the Subject of Who's on First

### On the Subject of Memory

### On the Subject of Morse Code

### On the Subject of Complicated Wires

### On the Subject of Wire Sequences

### On the Subject of Mazes

### On the Subject of Passwords

### On the Subject of Knobs
