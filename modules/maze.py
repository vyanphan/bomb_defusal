#!/usr/bin/env python3

'''
Only need 1 of the circle markers.
program maze solver (backtracking DFS with heuristic: manhattan distance, choose shorter direction first)

store maze picture as string
store maze as array of (NSEW) = (+1, -1, +1, -1)
if wall on S, e.g. (+1, 0, +1, -1)

keep tree of already traversed positions


return path and drawn path
for pos in array
    if array[pos]==2
        picture[pos] = '.'
'''

def prompt_maze():
    pass
