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
    
def clear():
    os.system("cls")


def prompt(options):
    """
    Gives the player a bunch of options and waits for his input.
    options - string list of action options. If string is "BLANK", skip a line.
        if string is NOOP: string, it will print string without options (Includes the space after NOOP:).
    
    returns a string of the option that the player picked.
    """
    key_assign = Key_assign()  # Used for assigning keys.
    #valid_input = ""  # Used for input validation.
    #keys_options_dict = {}  # Mapping keys to options. Used for returning the option.
    keys_list = []  # Store the keys used. Used for validation and returning option's index.
    
    print("")  # Skip a line for prettiness
    
    # Prompting the player with options.
    for option in options:
        # Special cases.
        if option == "BLANK":
            print("")
            continue
        if "NOOP: " in option:
            print(option[6:])
            continue

        key = key_assign.next()
        #valid_input += key
        keys_list.append(key)
        #keys_options_dict[key] = option  # Map key to option.
        
        print("{}: {}".format(key, option))
    
    # Read player's input.
    inp = getch()
    print(inp)  # Echo the input.
    # Input validation.
    while inp not in keys_list:
        print("Invalid input.")
        inp = getch()
        print(inp)
    
    return keys_list.index(inp)


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


if __name__ == "__main__":
    print(prompt(["Hi!", "BLANK", "NOOP: This line shouldn't have option", "Something else"]))
