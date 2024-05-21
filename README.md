AirBnB Clone - The Console
Description
Welcome to the AirBnB Clone project! This project is the first step towards building a full web application similar to AirBnB. In this initial phase, we develop a command interpreter to manage various AirBnB objects such as users, places, and more.

The command interpreter allows users to:

Create new objects
Retrieve objects from storage
Perform operations on objects
Update object attributes
Destroy objects
The interpreter operates both interactively and non-interactively, providing a versatile tool for managing the application’s data.

Command Interpreter
How to Start
To start the command interpreter, simply run the following command:

sh
Copy code
./console.py
How to Use
The interpreter provides a prompt (hbnb) where you can enter commands to interact with the AirBnB objects.

Commands
help: Lists available commands.
quit: Exits the command interpreter.
EOF: Exits the command interpreter (Ctrl+D).
Creating an Object
To create a new object, use the create command followed by the class name:

sh
Copy code
(hbnb) create <class>
Example:

sh
Copy code
(hbnb) create User
Showing an Object
To show an object, use the show command followed by the class name and object ID:

sh
Copy code
(hbnb) show <class> <id>
Example:

sh
Copy code
(hbnb) show User 1234-1234-1234
Destroying an Object
To destroy an object, use the destroy command followed by the class name and object ID:

sh
Copy code
(hbnb) destroy <class> <id>
Example:

sh
Copy code
(hbnb) destroy User 1234-1234-1234
Listing All Objects
To list all objects or all objects of a specific class, use the all command:

sh
Copy code
(hbnb) all <class>
Example:

sh
Copy code
(hbnb) all User
Updating an Object
To update an object’s attribute, use the update command followed by the class name, object ID, attribute name, and new value:

sh
Copy code
(hbnb) update <class> <id> <attribute> <value>
Example:

sh
Copy code
(hbnb) update User 1234-1234-1234 name "John Doe"
Examples
Start the command interpreter:
sh
Copy code
$ ./console.py
(hbnb)
Create a new User:
sh
Copy code
(hbnb) create User
Show a User with a specific ID:
sh
Copy code
(hbnb) show User 1234-1234-1234
Update a User’s attribute:
sh
Copy code
(hbnb) update User 1234-1234-1234 email "john.doe@example.com"
Destroy a User:
sh
Copy code
(hbnb) destroy User 1234-1234-1234
AUTHORS
This project is a collaborative effort by the following individuals:

Nonkanyiso Ndimande
For the format of this file, refer to Docker’s AUTHORS page.

Repository
GitHub repository: AirBnB_clone

Branches and Pull Requests
To collaborate effectively, we recommend using branches and pull requests. Each feature or fix should be developed in its own branch. When ready, submit a pull request to the main branch for review and merging.

AUTHORS File
graphql
Copy code
Nonkanyiso Ndimande <leighndimande17@icloud.com>
