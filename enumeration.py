

#### COME BACK TO THIS, VERY IMPORTANT, VERY USEFUL ####


from enum import Enum

# used to define symbolic names for when you
# want a restricted set of code-defined values
class FileAction(Enum):
    READ = 1  # choose any numbers
    WRITE = 2
    DELETE = 3

# simple class for doing file actions
class File:
    def __init__(self, actions):
        self.actions = actions

    def read(self):
        ...

    def write(self, something):
        ...

# define a file with restricted actions
readonly_file = File([FileAction.READ])

if (FileAction.WRITE in readonly_file.actions):
    print("writing to file...")
    readonly_file.write("hello")  # won't happen