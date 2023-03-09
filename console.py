#!/usr/bin/python3
import cmd
import sys
import os
import shlex
from models.base_model import BaseModel

classes = {'BaseModel': BaseModel}

class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '
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
        if argument in classes:
            print("mule i am creating")
        else:
            print("where is the arg")
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()