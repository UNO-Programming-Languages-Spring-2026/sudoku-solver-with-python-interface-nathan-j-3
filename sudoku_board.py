from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        rows = []

        for r in range(1, 10):
            row = []
            for c in range(1, 10):
                row.append(str(self.sudoku[(r, c)]))

            line = " ".join(row[0:3]) + "  " + " ".join(row[3:6]) + "  " + " ".join(row[6:9])
            rows.append(line)

            if r in (3, 6):
                rows.append("")

        return "\n".join(rows)

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        lines = s.strip().split("\n")

        for r, line in enumerate(lines, start=1):
            for c, ch in enumerate(line.strip(), start=1):
                if ch != ".":
                    sudoku[(r, c)] = int(ch)

        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}

        for atom in model.symbols(shown=True):
            if atom.name == "sudoku":
                r = atom.arguments[0].number
                c = atom.arguments[1].number
                v = atom.arguments[2].number
                sudoku[(r, c)] = v

        return cls(sudoku)
