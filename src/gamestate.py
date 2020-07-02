from board import Board


class GameState:
    board: Board

    def __init__(self, board):
        self.board = board

    @staticmethod
    def initial():
        board = Board.from_notation("[---,---,---]")
        return GameState(board)


gs = GameState.initial()

print(f"{gs.board.to_notation()=}")
print(f"{gs.board.from_notation('[123,456,789]')=}")
print(f"{gs.board.to_notation()=}")
