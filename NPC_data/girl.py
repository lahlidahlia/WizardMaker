"""
Defines a generic girl NPC class.
"""
import npc

class Girl(npc.NPC):
    def __init__(self):
        description = "Just a generic girl."
        name = "Girl"
        xml_file = "girl.xml"
        super(Girl, self).__init__(xml_file, name, description)

    def talk(self):
        if not self.met:
            self.dialogue_root = self.dialogue_root.find("./dialogue[@met]")
        else:
            self.dialogue_root = self.dialogue_root.find("./dialogue[not(@met)]")

        message = self.dialogue_root.find("./message").text
        self.print_message(message)

        

    def reset_dialogue(self):
        self.dialogue_root = self.xml_root
        
            

if __name__ == "__main__":
    Girl()
