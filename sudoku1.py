import sys
import clingo
from clingo.application import Application, clingo_main


class SudokuApp(Application):

    def main(self, control, files):

        # load sudoku encoding
        control.load("sudoku.lp")

        # load input instances
        for f in files:
            control.load(f)

        control.ground([("base", [])])

        control.solve()


if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])