from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, board):
        self.board = board
        self.sudoku = board  # ✅ ADD THIS LINE

    def __str__(self) -> str:
        lines = []

        for r in range(1, 10):
            row = [str(self.board[(r, c)]) for c in range(1, 10)]

            line = (
                " ".join(row[0:3]) + "  " +
                " ".join(row[3:6]) + "  " +
                " ".join(row[6:9])
            )
            lines.append(line)

            # blank line between blocks (but NOT after last block)
            if r in (3, 6):
                lines.append("")

        return "\n".join(lines)

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        board = {}
        lines = s.strip().split("\n")

        r = 1
        for line in lines:
            if line.strip() == "":
                continue  # skip blank lines between blocks

            tokens = line.split()
            for c, val in enumerate(tokens, start=1):
                if val != "-":
                    board[(r, c)] = int(val)

            r += 1

        return cls(board)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        board = {}

        for atom in model.symbols(shown=True):
            if atom.name == "sudoku":
                r = atom.arguments[0].number
                c = atom.arguments[1].number
                v = atom.arguments[2].number
                board[(r, c)] = v

        return cls(board)