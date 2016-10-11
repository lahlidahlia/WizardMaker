"""
Anh Huynh

This is the main file for the text adventure game.
"""

import input_prompt as inp
import os

if __name__ == "__main__":
    inp.clear()
    print("You see a road before your eyes. What do you do?")
    print(inp.prompt(["Follow path", "Die", "Prank someone"]))
    
    #JUST AS A NOTE, ESCAPE IS 27.