"""
Defines a generic girl NPC class.
"""
import npc
import xml.etree.ElementTree as ET

class Girl(npc.NPC):
    def __init__(self):
        description = "Just a generic girl."
        name = "Girl"
        xml_file = "girl.xml"
        super(Girl, self).__init__(xml_file, name, description)

        self.loop_message = None  # Dialogue is looped after NPC talks to NPC for
                          # the first time when entering the room.

    def talk(self):
        if not self.loop_message:
            if not self.met:
                self.dialogue_root = self.dialogue_root.find("./dialogue[@met='False']")
            else:
                self.dialogue_root = self.dialogue_root.find("./dialogue[@met='True']")
            message = self.dialogue_root.find("./message").text
            self.loop_message = self.dialogue_root.find("./loop").text
            self.print_message(message)
        else:
            self.print_message(self.loop_message)


        

    def reset_dialogue(self):
        """
        Triggered when player leaves the room.
        """
        self.dialogue_root = self.xml_root
        # It's better if NPC is considered "met" with player
        # after he leaves the room.
        if not self.met:
            self.met = True
        self.loop_message = None
        
            

if __name__ == "__main__":
    girl = Girl()
    girl.talk() 
    girl.talk()
    girl.talk()
    girl.reset_dialogue()
    girl.talk()
    girl.talk()
    girl.talk()

