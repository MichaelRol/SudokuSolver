"""Module for Sudoku classes."""
class Sudoku:
    """Class that defines a Sudoku object."""
    def __init__(self, problem):
        self.problem = problem

    def empty_remaining(self):
        """Returns number of empty squares remaining."""
        count = 0
        for r in self.problem:
            for c in r:
                if c == 0:
                    count += 1
        return count

    def is_complete(self):
        """Returns true if puzzle is completed, false otherwise."""
        if self.empty_remaining() == 0:
            return True
        return False

    def is_valid(self):
        """Returns True if puzzle is valid, false otherwise."""
        return  self.check_rows() and \
                self.check_cols() and \
                self.check_sqs()

    def check_rows(self):
        """Checks that there are no repeats within a row."""
        for row in self.problem:
            row = list(filter(lambda a: a != 0, row))
            if len(row) != len(set(row)):
                return False
        return True

    def check_cols(self):
        """Checks that there are no repeats within a column."""
        for i in range(0, len(self.problem[0])):
            col = [row[i] for row in self.problem]
            col = list(filter(lambda a: a != 0, col))
            if len(col) != len(set(col)):
                return False
        return True

    def check_sqs(self):
        """Checks that there are no repeats within a square."""
        for x_1 in range(0, 3):
            for y_1 in range(0, 3):
                square = []
                for x_2 in range(0, 3):
                    for y_2 in range(0, 3):
                        square.append(self.problem[x_1*3+x_2][y_1*3+y_2])
                square = list(filter(lambda a: a != 0, square))
                if len(square) != len(set(square)):
                    return False
        return True

    def __str__(self):
        output = ""
        counter_r = 0
        num_row_lines = 0
        for r in self.problem:
            counter_c = 0
            num_col_lines = 0
            for c in r:
                if c != 0:
                    output += str(c) + " "
                else:
                    output += "  "
                if counter_c == 2 and num_col_lines < 2:
                    output += "| "
                    num_col_lines += 1
                counter_c = (counter_c + 1) % 3
            if counter_r == 2 and num_row_lines < 2:
                output += "\n" + "-"*22+"\n"
                num_row_lines += 1
            else:
                output += "\n"
            counter_r = (counter_r + 1) % 3
        return output
