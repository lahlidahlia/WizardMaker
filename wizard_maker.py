"""
Anh Huynh

This is the main file for the text adventure game.
"""

import print_prompt as pp
import locations
from player import Player
import os
import npc
import girl
import os

if __name__ == "__main__":
    player = Player()

    pp.clear()
    room1 = locations.Room("room1", "You see a road before your eyes. What do you do?")
    room1.print_description()
    #print(pp.prompt(["Follow path", "Die", "Prank someone"]))

    room2 = locations.Room("room2", "You followed the path.")
    grill = girl.Girl()
    room2.npc_in_room.append(grill)
    room2.print_description()
    room2.construct_options()

    #JUST AS A NOTE, ESCAPE IS 27.
