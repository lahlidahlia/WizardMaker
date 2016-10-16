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
    room2 = locations.Room("room2", "You followed the path.")

    room1.connected_rooms.append(room2)
    room2.connected_rooms.append(room1)
    room2.npc_in_room.append(girl.Girl())

    room1.player_enter_room()


    #JUST AS A NOTE, ESCAPE IS 27.
