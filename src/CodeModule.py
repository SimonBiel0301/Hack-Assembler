class CodeModule:
    destDictionary = {"null": '000', "M": '001', "D": '010', "MD": '011', "A": '100', "AM": '101', "AD": '110',
                      "AMD": '111'}

    compDictionary = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "1+D": "0011111",
        "A+1": "0110111",
        "1+A": "0011111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "A+D": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "A&D": "0000000",
        "A|D": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "1+M": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "M+D": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "M&D": "1000000",
        "D|M": "1010101",
        "M|D": "1010101"

    }

    jumpList = ["null", "JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"]

    def __init__(self):
        print("Instance of Code-Module created")

    def dest(self, input):
        try:
            #print("dest: " + self.destDictionary[input])
            return self.destDictionary[input]
        except:
            return '000'

    def comp(self, input):
        try:
            #print("comp: " + self.compDictionary[input])
            return self.compDictionary[input]
        except:
            return '000'

    def jump(self, input):
        try:
            #print("jump: " + str(format(self.jumpList.index(input.strip()), "b")))
            return self.jumpList.index(input.strip())
        except:
            return '000'
