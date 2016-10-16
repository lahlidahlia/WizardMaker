"""
Deals with anything to do with locations. Implements the overworld map, rooms, their descriptions, events, interactions, etc...
"""
import print_prompt as pp

class Room:
    """
    Implements a single room and its description, events, interactions. A room is any location 
     that can be indoor or outdoor. Anything.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description  # General description of the room.
        self.connected_rooms = []  # Rooms that you can travel to from here.
        self.npc_in_room = []  # NPCs currently in this room (can change).
        self.events = []  # Events that can trigger. 

    def print_description(self):
        print("")
        print(self.description)
        print("You see {} here".format(" ".join([npc.name for npc in self.npc_in_room])))

    def player_enter_room(self):
        """
        Called whenever the player enters this room.
        """
        print_description()
        
    def construct_options(self):
        """
        Construct some options for the player when he enters the room.

        Run the option player chooses as well. Returning it would be such a pain.
        """
        options = []
        actions = []  # Functions to execute based on option.
                      # Functions are stored as reference to be executed later.
        # Movement options
        options.append("NOOP: Move to:")
        for room in self.connected_rooms:
            options.append("{}".format(room.name))
            actions.append(room.move_to)
        # Talking options
        options.append("BLANK")
        options.append("NOOP: Talk to:")
        for npc in self.npc_in_room:
            options.append("{}".format(npc.name))
            actions.append(npc.talk)
        # Looking options
        options.append("BLANK")
        options.append("NOOP: Look at:")
        for npc in self.npc_in_room:
            options.append("{}".format(npc.name))
            actions.append(npc.print_description)
        # Menu
        options.append("BLANK")
        options.append("BLANK")
        options.append("Menu")
        actions.append(lambda: None)  #TODO

        #Prompt
        choice = pp.prompt(options)
        actions[choice]()  # Execute the option.
