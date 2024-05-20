#!/usr/bin/python3
import cmd
from models.user import User

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
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        class_name = arg_list[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])


    def do_destroy(self,arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = f"{arg_list[0]}. {arg_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del strorage.all()[key]
        storage.save

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not args:
            obj_list = [str(obj) for obj in storage.all().values()]
        else:
            if args not in storage.classes():
                print("** class doesn't exist **")
                return
            obj_list = [str(obj) for obj in storage.all().values() if type(obj).__name__ == args]
        print(obj_list)

        
     def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        arg_list = args
        rg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        instance = storage.all()[key]
        setattr(instance, arg_list[2], arg_list[3].strip('"'))
        instance.save()

    def do_help(self, arg):
        """Help command to display available commands"""
        cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
