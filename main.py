"""Module for running of Sudoku code."""
import sys
import csv
import sudoku
import solver

problem_array = [[5, 1, 8, 6, 0, 0, 4, 0, 0],
                [0, 0, 6, 0, 0, 0, 0, 0, 7],
                [4, 3, 0, 2, 0, 0, 0, 0, 6],
                [7, 0, 0, 0, 0, 0, 0, 3, 0],
                [0, 6, 4, 0, 1, 8, 2, 0, 5],
                [0, 5, 0, 7, 2, 6, 9, 4, 8],
                [0, 0, 9, 0, 0, 1, 8, 2, 3],
                [0, 2, 1, 0, 0, 0, 7, 0, 0],
                [3, 0, 0, 0, 4, 0, 0, 6, 9]]

def problem_from_csv(csv_path):
    """Read in CSV file and produce Sudoku object."""
    with open(csv_path, newline='\n', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        puzzle = []
        for row in csv_reader:
            puzzle.append(list(map(int, row)))
    parsed_sudoku = sudoku.Sudoku(puzzle)
    if parsed_sudoku.is_valid():
        return parsed_sudoku
    raise Exception("ERROR: Parsed Sudoku is not valid.")


if __name__ == "__main__":
    a_solver = solver.Solver()
    if len(sys.argv) == 1:
        print("INFO: No CSV file provided. Using default problem.")
        problem = sudoku.Sudoku(problem_array)
        print(a_solver.solve(problem))
    elif len(sys.argv) == 2:
        print("INFO: Loading CSV puzzle.")
        problem = problem_from_csv(sys.argv[1])
        print(a_solver.solve(problem))
    else:
        print("ERROR: Too many arguments. Please enter the path to a csv file.")
