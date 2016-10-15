"""
Handles input prompting and parsing.

Contained here: class Key_assign, clear(), prompt(options),
"""
import os
import platform

if platform.system() == "Linux":
    from getch import getch
elif platform.system() == "Windows":
    from msvcrt import getch

class Key_assign:
    """
    Manager for assigning keys to options. Optimized for left hand use on the keyboard.
    """
    def __init__(self):
        self.key_assign_order = "12345qwertasdfgzxcvb67890yuiohjklnm,."  # Keys get assigned to options in this order.
        self.key_index = 0  # Which key to be used next, based off of key_assign_order.
    
    def next(self):
        """
        Returns the next key in the order list.
        """
        ret = self.key_assign_order[self.key_index]
        self.key_index += 1
        return ret
    
def clear():
    os.system("cls")


def prompt(options):
    """
    Gives the player a bunch of options and waits for his input.
    options - string list of action options.
    
    returns a string of the option that the player picked.
    """
    key_assign = Key_assign()  # Used for assigning keys.
    valid_input = ""  # Used for input validation.
    keys_options_dict = {}  # Mapping keys to options. Used for returning the option.
    
    print("")  # Skip a line for prettiness
    
    # Prompting the player with options.
    for option in options:
        key = key_assign.next()
        
        valid_input += key
        keys_options_dict[key] = option  # Map key to option.
        
        print("{}: {}".format(key, option))
    
    # Read player's input.
    inp = getch()
    print(inp)  # Echo the input.
    while inp not in valid_input:
        print("Invalid input.")
        inp = getch()
        print(inp)
    
    return keys_options_dict[inp]
    

if __name__ == "__main__":
    print(getch())
