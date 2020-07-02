from board import Board


class GameState:
    board: Board

    def __init__(self, board):
        self.board = board

    @staticmethod
    def initial():
        board = Board.from_notation("[---,---,---]")
        return GameState(board)
