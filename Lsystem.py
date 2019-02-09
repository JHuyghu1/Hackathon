class Lsystem:
    def __init__(self,filename):
        try:
            self.lsys = open(filename, "r")
        except FileNotFoundError:
            print("File Doesn't Exist")
        else:
            self.angle = int(self.lsys.readline())
            self.iteration = int(self.lsys.readline())
            self.distance = int(self.lsys.readline())
            self.axiom = self.lsys.readline()
            self.rules = {}
            self.state = []
            while True:
                rul = self.lsys.readline()
                if not rul:
                    break
                symbol = rul[0]
                sub = rul[4:(len(rul)-1)]
                self.rules[symbol] = sub
            self.lsys.close()

    def createLsystem(self):
        pass

    def applyRules(self,string):
        pass

    def drawLSystem(self, snap):
        pass
