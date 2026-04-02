import sys
import clingo
from clingo.application import Application, clingo_main


class SudokuApp(Application):

    def main(self, control, files):
        control.load("sudoku.lp")

        for f in files:
            control.load(f)

        control.ground([("base", [])])
        control.solve()

    def print_model(self, model, printer):
        atoms = sorted(str(a) for a in model.symbols(shown=True))
        print(" ".join(atoms))


if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])