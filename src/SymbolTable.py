class SymbolTable:
    table = {
        "SP" : 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576,
    }
    nextRamAdress = 16

    def __init__(self):
        print("Instance of Symbol Table created")

    def contains(self, label):
        if label in self.table or "R" in label:
            return True
        else:
            return False

    def addEntry(self, symbol):
        self.table[symbol] = self.nextRamAdress
        self.nextRamAdress += 1

    def addL_COMMAND(self, symbol, adress):
        self.table[symbol.strip()] = adress

    def getAdress(self, symbol):
        if symbol.strip() in self.table:
            return self.table[symbol]
        # Else: symbol is Rxx
        else:
            if len(symbol) == 2:
                return int(symbol[1])
            else:
                return int(symbol[1:3])