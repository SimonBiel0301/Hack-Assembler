from typing import List, Any

from SymbolTable import SymbolTable
from Parser import Parser
from CodeModule import CodeModule
from os.path import exists
from pathlib import Path


def assemblersAssemble():
    provisorischeListeAlsOutput = []
    symbolTable = SymbolTable()
    codeModule = CodeModule()
    #type = input("Do you want to read the file from the current directory (C/c), or from another one (A/a)")
    print("------------------------------")
    filename = input("Please input the filename of the .asm file to be converted. It must be in this directory")
    print("------------------------------")
    filePath = Path.cwd().joinpath(filename)
    if not exists(filePath):
        print("Given file does not exist in: '", filePath, "'")
        print("Terminating the programm.........")
        print("------------------------------")
        return

    parser = Parser(filePath)

    print("Beginning with the first Pass")
    firstPass(symbolTable, parser)
    parser.currentCommandCounter = 0
    parser.currentCommand = parser.file[0]
    print("Beginning with the second Pass")
    secondPass(symbolTable, parser, codeModule, provisorischeListeAlsOutput)
    print("------------------------------")
    print("Finished assembly process")
    print("Lines of Binary Code: "+str(len(provisorischeListeAlsOutput)))
    print(filename[0:len(filename)-3]+"hack"+ " added to the directory")
    print("Terminating Hack-Assembler")
    print("------------------------------")
    print("------------------------------")

    output = open(filename[0:len(filename)-3]+"hack", "w")
    for line in provisorischeListeAlsOutput:
        output.write(line+"\n")
    output.close()

def firstPass(symbolTable, parser):
    '''
    The first pass needs to add a label for all (LABEL)
    :param table: used SymbolTable
    :param parser: used Parser
    '''
    # Way to keep track of how many lines the address value of a label has to be decremented
    dec = 0



    # Check first command for (LABEL)
    if parser.commandType() == "L_COMMAND":
        label = parser.symbol()
        symbolTable.addL_COMMAND(label, 1)
        dec += 1


    # loop over rest
    codeIndex = 1
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == "L_COMMAND":
            label = parser.symbol()
            adress = codeIndex-dec
            symbolTable.addL_COMMAND(label, adress)
            dec += 1

        codeIndex += 1


def secondPass(symbolTable, parser, codeModule, outputList):
    '''
    The second pass needs to translate each other line
    :param table:
    :param parser:
    :return:
    '''

    # Check first line
    processCommand(symbolTable, parser, codeModule, outputList)
    # Loop over rest of lines
    while parser.hasMoreCommands():
        parser.advance()
        processCommand(symbolTable, parser, codeModule, outputList)

    # Output new Programm
    #for x in outputList:
    #    print(x)


def processCommand(symbolTable, parser, codeModule, outputList):
    expression = ""
    # C-Instruction

    if parser.commandType() == "C_COMMAND":
        #print("Is a C_COMMAND")
        expression = "111"

        # Create binary Strings for comp, dest and jump
        comp = parser.comp().strip()
        #print("comp: "+comp)
        compString = codeModule.comp(comp)
        dest = parser.dest().strip()
        #print("dest: " + dest)
        destString = codeModule.dest(dest)
        jump = parser.jump().strip()
        #print("jump: " + jump)
        jumpString = make3BitString(codeModule.jump(jump))

        # Append Strings in order: comp, dest, jump
        expression = expression + compString + destString + jumpString
        #print("expression: "+ expression)


    # A-Instruction
    else:
        if parser.commandType() == "L_COMMAND":
            return

        #print("Is a A_COMMAND")
        symbol = parser.symbol().strip()
        # Value given to write to A
        if symbol.isdigit():
            #print("Is numeric")
            value = make15BitString(int(parser.symbol()))

        # Variable given to write to A
        else:
            #print("Is Variable")
            # variable does not exist
            if not symbolTable.contains(symbol):
                symbolTable.addEntry(symbol)

            # write value as binary
            value = symbolTable.getAdress(symbol)
            #print("Value: " +str(value))
            value = make15BitString(value)

        # create A-Expression:
        expression = str(0)+value
        #print("expression: "+expression)
    outputList.append(expression)


def make16BitString(valueInt):
    value = format(valueInt, "b")
    # If binary represantation is larger than 15 bits -> Delete some of the msb
    if len(value) > 16:
        difference = len(value) - 16
        value = value[difference:len(value)]
    # if its smaller than 15 bits -> add bits at the front
    if len(value) < 16:
        difference = 16 - len(value)
        toAdd = str(0) * difference
        value = toAdd + value
    return value


def make15BitString(valueInt):
    value = format(valueInt, "b")
    # If binary represantation is larger than 15 bits -> Delete some of the msb
    if len(value) > 15:
        difference = len(value) - 15
        value = value[difference:len(value)]
    # if its smaller than 15 bits -> add bits at the front
    if len(value) < 15:
        difference = 15 - len(value)
        toAdd = str(0) * difference
        value = toAdd + value
    return value

def make3BitString(valueInt):
    value = format(valueInt, "b")
    # If binary represantation is larger than 15 bits -> Delete some of the msb
    if len(value) > 3:
        difference = len(value) - 3
        value = value[difference:len(value)]
    # if its smaller than 15 bits -> add bits at the front
    if len(value) < 3:
        difference = 3 - len(value)
        toAdd = str(0) * difference
        value = toAdd + value
    return value


if __name__ == '__main__':
    print("------------------------------")
    print("------------------------------")
    print("Assemblers ....... assemble!!!")
    assemblersAssemble()
