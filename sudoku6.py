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
                    "",  # IMPORTANT: empty name
                    [clingo.Number(r), clingo.Number(c), clingo.Number(v)]
                )
            )
        return result


class SudokuApp(Application):

    def main(self, control, files):
        # read txt input
        with open(files[0]) as f:
            content = f.read()

        sudoku = Sudoku.from_str(content)
        ctx = Context(sudoku)

        # load ASP files
        control.load("sudoku.lp")
        control.load("sudoku_py.lp")

        # ground with context
        control.ground([("base", [])], context=ctx)

        # only one solution
        control.configuration.solve.models = 1

        control.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)


if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])