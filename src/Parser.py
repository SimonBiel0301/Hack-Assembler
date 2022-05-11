from pathlib import Path
from os import chdir
class Parser:
    file = list
    currentCommandCounter = 0
    lastCommandIndex = 0
    currentCommand = ""


    def __init__(self, filepath):
        '''
        :param filename: name of the .asm file to be assembled
        Initializer for Parser. Reads the given file.
        '''
        print('Parser initialized.')
        print('Trying to read file ', filepath)

        try:
            target = filepath
        except:
            print("Oops, something went wrong reading the filename :(")
        else:
            with open(target) as f:
                self.file = f.readlines()
                newFile = []
                # Check all lines
                for line in self.file:
                    # Remove whitespaces
                    line = line.replace(" ", "")
                    # Remove comments
                    if "//" in line:
                        if line.index("//") == 0:
                            line = ""
                        else:
                            line = line[0:line.index("//")]
                    # Remove empty lines
                    if not len(line.strip()) == 0:
                        newFile.append(line)
                f.close()

                self.file = newFile

            self.lastCommandIndex = len(self.file) - 1
            self.currentCommand = self.file[0]

    def hasMoreCommands(self):
        '''
        :returns True, if there are commands in the file left. Else returns False
        '''
        return self.currentCommandCounter < self.lastCommandIndex

    def advance(self):
        self.currentCommandCounter += 1
        self.currentCommand = self.file[self.currentCommandCounter]

    def commandType(self):
        command = self.currentCommand
        if command[0] == "@":
            return "A_COMMAND"
        elif command[0] == "(":
            return "L_COMMAND"
        else:
            return "C_COMMAND"

    def symbol(self):
        # read current command
        command = self.currentCommand
        command = command.replace("@","")
        command = command.replace("(","")
        command = command.replace(")","")
        return command

    def dest(self):
        command = self.currentCommand
        # Needs to check if dest is null -> If there is an "=" in the String, there also is a destination
        if "=" in command:
            indexEquals = command.find("=")
            return command[0:indexEquals]
        else:
            return "null"

    def comp(self):
        command = self.currentCommand
        startIndex = 0
        endIndex = len(command)
        if "=" in command:
            startIndex = command.find("=")+1
        if ";" in command:
            endIndex = command.find(";")

        # Return remainder
        return command[startIndex:endIndex]

    def jump(self):
        command = self.currentCommand
        if ";" in command:
            index = command.find(";")
            return command[index+1:len(command)]
        else:
            return "null"