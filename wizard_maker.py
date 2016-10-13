"""
Anh Huynh

This is the main file for the text adventure game.
"""

import input_prompt as inp
import locations
import os

if __name__ == "__main__":
    inp.clear()
    room1 = locations.Room("You see a road before your eyes. What do you do?")
    room1.print_description()
    print(inp.prompt(["Follow path", "Die", "Prank someone"]))
    
    #JUST AS A NOTE, ESCAPE IS 27.
