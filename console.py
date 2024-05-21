#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance, saves it and prints"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")


    def do_destroy(self,arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        instances = []
        if args and args[0] in globals():
            class_name = args[0]
            for key, value in storage.all().items():
                if class_name in key:
                    instances.append(str(value))
            print(instances)
        elif not args:
            for value in storage.all().values():
                instances.append(str(value))
            print(instances)
        else:
            print("** class doesn't exist **")
        
     def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        value = args[3]
        obj = storage.all()[key]
        setattr(obj, attribute_name, value)
        obj.save()

    def default(self, line):
        """Catches unknown commands and tries to handle <class name>.all()"""
        args = line.split('.')
        if len(args) == 2:
             class_name = args[0]
            command = args[1]
            if command == "all()":
                if class_name in globals():
                    self.do_all(class_name)
                else:
                    print("** class doesn't exist **")
            elif command == "count()":
                if class_name in globals():
                    self.do_count(class_name)
                else:
                    print("** class doesn't exist **")
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, class_name):
        """Counts the number of instances of a class"""
        count = 0
        for key in storage.all().keys():
            if key.startswith(class_name + '.'):
                count += 1
        print(count)

    def do_help(self, arg):
        """Help command to display available commands"""
        cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
