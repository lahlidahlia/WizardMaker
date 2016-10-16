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
        self.player_in_room = False  # Is the player in this room.

    def print_description(self):
        """
        Print the description of this room and everything in it.
        """
        print("")
        print(self.description)
        print("You see {} here".format(" ".join([npc.name for npc in self.npc_in_room])))

    def move_to(self):
        """
        Move the player to this room.
        """
        self.player_enter_room()

    def player_enter_room(self):
        """
        Called whenever the player enters this room.
        """
        self.print_description()
        self.player_in_room = True
        self.construct_options()
        
    def player_leave_room(self):
        """
        Called whenever the player leave the room.
        """
        for npc in self.npc_in_room:
            npc.reset_dialogue()
        self.player_in_room = False

    def construct_options(self):
        """
        Construct some options for the player when he enters the room.

        Run the option player chooses as well. Returning it would be such a pain.
        """
        options = []
        actions = []  # Functions to execute based on option.
                      # Functions are stored as reference to be executed later.
                      # Also stored as list in a list to support executing multiple
                      #functions at once.
        # Movement options
        options.append("NOOP: Move to:")
        for room in self.connected_rooms:
            options.append("{}".format(room.name))
            actions.append([self.player_leave_room, room.player_enter_room])
        # Talking options
        options.append("BLANK")
        options.append("NOOP: Talk to:")
        for npc in self.npc_in_room:
            options.append("{}".format(npc.name))
            actions.append([npc.talk])
        # Looking options
        options.append("BLANK")
        options.append("NOOP: Look at:")
        for npc in self.npc_in_room:
            options.append("{}".format(npc.name))
            actions.append([npc.print_description])
        # Menu
        options.append("BLANK")
        options.append("BLANK")
        options.append("Menu")
        actions.append([lambda: None])  #TODO

        #Prompt
        choice = pp.prompt(options)
        for action in actions[choice]:
            action() # Execute the actions
