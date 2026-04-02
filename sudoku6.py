import sys
import clingo
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku


class Context:

    def __init__(self, board):
        self.board = board

    def initial(self):
        result = []

        for (r, c), v in self.board.board.items():
            result.append(
                clingo.Function(
                    "",   # ✅ EMPTY NAME (THIS WAS THE BUG)
                    [clingo.Number(r), clingo.Number(c), clingo.Number(v)]
                )
            )

        return result


class SudokuApp(Application):

    def main(self, control, files):
        # read txt file
        with open(files[0]) as f:
            content = f.read()

        sudoku = Sudoku.from_str(content)

        ctx = Context(sudoku)

        control.load("sudoku.lp")
        control.load("sudoku_py.lp")

        control.ground([("base", [])], context=ctx)

        control.configuration.solve.models = 1

        control.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)


if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])