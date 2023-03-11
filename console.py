#!/usr/bin/python3
import cmd
import sys
import os
import shlex
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}


class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}
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
                get_class = getattr(sys.modules[__name__], x[0])
                if len(x) >= 2:
                    dic = models.storage.all()
                    # Key has format <className>.id
                    key = x[0] + '.' + x[1]
                    if key in dic:
                        print(dic[key])
                        return
                    else:
                        print("** no instance found **")
                        return
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    def do_destroy(self, argument):
        """Deletes an instance based on the class name and id"""
        if argument:
            x = argument.split()
            if x[0] in self.classes:
                if len(x) >= 2:
                    dic = models.storage.all()
                    # Key has format <className>.id
                    key = x[0] + '.' + x[1]
                    if key in dic:
                        del dic[key]
                        models.storage.save()
                        return
                    else:
                        print("** no instance found **")         
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, argument):
        """Deletes an instance based on the class name and id"""
        if argument:
            dic = models.storage.all()
            x = argument.split()
            my_list = []
            if x[0] in self.classes:
                for key in dic:
                    y = str(dic[key])
                    #my_list.append(x)
                    class_type = key.split('.')
                    if x[0] in class_type[0]:
                        my_list.append(y)

                print(my_list)
            else:
                print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            my_list = []
            for key in dic:
                x = str(dic[key])
                my_list.append(x)
            print(my_list)
    
    def do_update(self, argument):
        """Updates an instance based on the class name and id """
        if argument:
            x = shlex.split(argument)
            if x[0] in self.classes:
                if len(x) >= 2:
                    dic = models.storage.all()
                    key = x[0] + '.' + x[1]
                    if key in dic:
                        if len(x) >= 3:
                            m = dic[key]
                            key2 = x[0] + '.' + x[1] + '.' + x[2]
                            if len(x) >= 4:
                                typeA = type(getattr(dic[key], x[2]))
                                x[3] = typeA(x[3])
                                print(type(x[3]))
                                setattr(m, x[2], x[3])
                                models.storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        
    def precmd(self, argument):
        """ executed just before the command line line is interpreted """
        if argument:
            x = argument.split('.')
            if x[0] in self.classes:
                if '("' in x[1]:
                    y = x[1].split('("')
                    if '", ' in y[1]:
                        z = y[1].split('")')
                        k = z[0].split('",')
                        j = k[1].split('"')
                        i = k[2].split('"')
                        command = y[0] + ' ' + x[0] + ' ' + k[0] + ' ' + j[1] + ' ' + i[1]

                    else:
                        z = y[1].split('")')
                        command = y[0] + ' ' + x[0] + ' ' + z[0]
                        return command 
                else:
                    y = x[1].split('(')
                    command = y[0] + ' ' + x[0]
                    return command
            else:
                return argument
    def do_count(self, argument):
        """ executed just before the command line line is interpreted """
        dic = models.storage.all()
        count = 0
        if argument:
            x = argument.split(' ')
            if x[0] in self.classes:
                for key in dic:
                    y = key.split('.')
                    if y[0] in x[0]:
                        count = count + 1
                print(count)
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
