"""
Deals with anything to do with locations. Implements the overworld map, rooms, their descriptions, events, interactions, etc...
"""

class Room:
    """
    Implements a single room and its description, events, interactions. A room is any location 
     that can be indoor or outdoor. Anything.
    """
    def __init__(self, description):
        self.description = description  # General description of the room.
        self.connected_rooms = []  # Rooms that you can travel to from here.
        self.npc_in_room = []  # NPCs currently in this room (can change).
        self.events = []  # Events that can trigger. 

    def print_description(self):
        print("")
        print(self.description)
        print("You see {} here".format(" ".join([npc.name for npc in self.npc_in_room])))
