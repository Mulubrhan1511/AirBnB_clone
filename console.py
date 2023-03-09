#!/usr/bin/python3
import cmd
import sys
import os
import shlex
import models
from models.base_model import BaseModel




class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'BaseModel': BaseModel}
    def do_quit(self, argument):
        """ Defines quit option"""
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True
    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")
    def do_ENTER(self):
        """ Prints help command description """
        pass
    def do_create(self, argument):
        """Creates an instance of BaseModel"""
        if argument:
            #if there is an argument
            if argument in self.classes:
                get_class = getattr(sys.modules[__name__], argument)
                mule = get_class()
                print(mule.id)
                models.storage.save()
                return
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
    def do_show(self, argument):
        """Prints the string representation of an instance based on the class name and id"""
        if argument:
            #if there is argument
            x = argument.split()
            if x[0] in self.classes:
                print("showing...")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()