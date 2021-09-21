"""Module for solving sudoku puzzles."""
class Solver:
    """Class for solving sudoku puzzles."""

    def solve(self, sudoku):
        """Method for solving Sudoku problems."""
        left_to_solve = sudoku.empty_remaining()
        while not sudoku.is_complete():
            for r, _ in enumerate(sudoku.problem):
                for c, _ in enumerate(sudoku.problem[0]):
                    if sudoku.problem[r][c] == 0:
                        possibilities = self.find_possibilities(sudoku, r, c)
                        if len(possibilities) == 1:
                            sudoku.problem[r][c] = possibilities[0]
                        if len(possibilities) == 0:
                            raise Exception("ERROR: No possibilities could be found. Invalid problem.")
            if left_to_solve == sudoku.empty_remaining():
                if not self.backtrack(sudoku):
                    raise Exception("ERROR: Backtracking could not solve puzzle, it must be invalid.")
                return sudoku
            left_to_solve = sudoku.empty_remaining()
        if not sudoku.is_valid():
            raise Exception("ERROR: Puzzle completed but is invalid.")
        return sudoku

    def backtrack(self, sudoku):
        """Backtracking algorithm for brute-force solving of Sudoku problems."""
        if sudoku.is_complete():
            return True
        empty = self.find_empty(sudoku.problem)
        for guess in range(1, 10):
            sudoku.problem[empty[0]][empty[1]] = guess
            if sudoku.is_valid():
                if self.backtrack(sudoku):
                    return True
            sudoku.problem[empty[0]][empty[1]] = 0
        return False


    @staticmethod
    def find_empty(sudoku):
        """Finds first empty square"""
        for r, _ in enumerate(sudoku):
            for c, _ in enumerate(sudoku[0]):
                if sudoku[r][c] == 0:
                    return [r, c]
        return [0, 0]

    @staticmethod
    def find_possibilities(sudoku, r, c):
        """Method for finding possible values of a blank square."""
        possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for element in sudoku.problem[r]:
            if element in possibilities:
                possibilities.remove(element)
        for index in range(0, 9):
            if sudoku.problem[index][c] in possibilities:
                possibilities.remove(sudoku.problem[index][c])
        start_r = 0
        start_c = 0
        if r > 2:
            start_r = 3
        if r > 5:
            start_r = 6
        if c > 2:
            start_c = 3
        if c > 5:
            start_c = 6
        for new_r in range(start_r, start_r + 3):
            for new_c in range(start_c, start_c + 3):
                if sudoku.problem[new_r][new_c] in possibilities:
                    possibilities.remove(sudoku.problem[new_r][new_c])
        return possibilities
