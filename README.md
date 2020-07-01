# AirBnb_clone
## Description of the project
The first part of the AirBnb_clone, here creates a command-line interpreter that works as the core of the back-end side. The console is connected to storage engines that keeps the database and the file storage. By the way this part were focused on the file storage management.
## Description of the command-line interpreter:
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine.
## How to use it
*Command* | *Usage* | *Example* | *Description*
--- | --- | --- | ---
help | help | help | Displays a list of the commands
create | create \<class\> | create User | Creates a new instance of the class
show | show \<class\> \<id\> | show User 123-123-123 | Shows a specific instance
destroy | destroy \<class\> \<id\> | destroy User 123-123-123 | Destroy a specific instance
all | all or all \<class\> | all User | Shows all the instances created
update | update \<class\> \<id\> \<attribute\> \<value\> | update User 123-123-123 email 'email@mail' | Updates an instance attribute
count | \<class\>.count | User.count | Counts the number of an instance
quit | quit | quit | Quits the console
## Examples
### Interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
### Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ echo "create User" | ./console.py 
(hbnb) 36999f0d-c1b7-49ed-bd6b-2672e38ec725
(hbnb)
$
$ echo "show User 36999f0d-c1b7-49ed-bd6b-2672e38ec725" | ./console.py
(hbnb) [User] (36999f0d-c1b7-49ed-bd6b-2672e38ec725) {'created_at': datetime.datetime(2020, 7, 1, 18, 45, 24, 751121), 'update_at': datetime.datetime(2020, 7, 1, 18, 45, 24, 751145), 'id': '36999f0d-c1b7-49ed-bd6b-2672e38ec725'}
(hbnb) 
$
```
## Setup
+ Interpreter: Python 3
+ S.O: Interpreted/compiled on Ubuntu 14.04 LTS
+ Style: pep8 ver 1.7.1