# Keep Talking and Nobody Explodes
==================================

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
- If at any moment you messed up, use the command `restart` to clear the module.
- When prompted, type the name of the module.
- The input is not case-sensitive, but make sure to use the formats as described below.

### Wires (Simple)
- When the prompt appears, enter the colors of the wires in top-down order, separated by spaces.
- Pros who want to break a speed challenge can enter the color codes of the wires.
	- blue: B
	- red: R
	- yellow: Y
	- black: K
	- white: W
- If the prompt asks for the serial number simply enter it as shown on the bomb. 

