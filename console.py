#!/usr/bin/python3
"""
 console module

"""
import cmd 
from models.base_model import BaseMode1

class HBNBCommand(cmd.Cmd):

    """
    HBNBComand class
    """
    def EOF(self, line):
        """handles EOF"""
        return True

    def QUIT(self, line):
        """Quit command to exit the program"""
        return True

    def MT_LINE(self):
        """an empty line"""
        pass

    def CREATE(self, line):
        """Creates a solution for emptylines and spaces"""
        if line == "" or line is None:
            print("** class name missing **")





    if __name__ == '__main__':
        HBNBCommand().cmdloop()