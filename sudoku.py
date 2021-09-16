class Sudoku:
    def __init__(self, problem):
        self.problem = problem

    def empty_remaining(self):
        count = 0
        for r in self.problem:
            for c in r:
                if c == 0:
                    count += 1 
        return count
    
    def is_complete(self):
        if self.empty_remaining() == 0:
            return True
        return False

    def __str__(self):
        output = ""
        counterR = 0
        numRowLines = 0
        for r in self.problem:
            counterC = 0
            numColLines = 0
            for c in r:
                if c != 0:
                    output += str(c) + " "
                else:
                    output += "  "
                if counterC == 2 and numColLines < 2:
                    output += "| "
                    numColLines += 1
                counterC = (counterC + 1) % 3
            if counterR == 2 and numRowLines < 2:
                output += "\n" + "-"*22+"\n"
                numRowLines += 1
            else:
                output += "\n"
            counterR = (counterR + 1) % 3
        return output


