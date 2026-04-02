import sys
import clingo
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku


class SudokuApp(Application):

    def main(self, control, files):
        control.load("sudoku.lp")

        for f in files:
            control.load(f)

        control.ground([("base", [])])

        control.configuration.solve.models = 1

        control.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)


if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])