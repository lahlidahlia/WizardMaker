"""
This file deals with NPCs. Talking to NPCs, their descriptions, interactions etc...
"""
import xml.etree.ElementTree as ET
import os

class NPC(object):
    """
    Abstract class. Must implement talk.
    """
    def __init__(self, xml_file, name, description):
        """
        xml_file : string = Name of the file. Do not include a path.
        name : string = Name of the NPC.
        description : string = Description of the NPC.
        """
        self.met = False  # Has the NPC met the player?
        self.name = name
        self.description = description

        path = os.path.dirname(__file__)
        self.xml_root = ET.parse(path + "/" + xml_file).getroot()  # Original copy
        self.dialogue_root = self.xml_root  # Used for xml traversing

        
    def talk(self):
        """
        The player talks to this NPC.

        Abstract method.
        """
        raise NotImplementedError

    def print_message(self, text):
        print "{}: {}".format(self.name, text)
        
