import sudoku

class Solver:
    def __init__(self, problem):
        self.problem = problem

problemArray = [[5, 1, 8, 6, 0, 0, 4, 0, 0],
                [0, 0, 6, 0, 0, 0, 0, 0, 7],
                [4, 3, 0, 2, 0, 0, 0, 0, 6],
                [7, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 6, 4, 0, 1, 8, 2, 0, 5],
                [0, 5, 0, 7, 2, 6, 9, 4, 8],
                [0, 0, 9, 0, 0, 1, 8, 2, 3],
                [0, 2, 1, 0, 0, 0, 7, 0, 0],
                [3, 0, 0, 0, 4, 0, 0, 6, 9]]

problem = sudoku.Sudoku(problemArray)
print(problem.is_complete())
print(problem.empty_remaining())
print(problem)