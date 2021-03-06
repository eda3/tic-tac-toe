from __future__ import annotations

from board import Board


class GameState:
    board: Board

    def __init__(self, board: Board) -> None:
        self.board = board

    @staticmethod
    def initial() -> GameState:
        board = Board.from_notation("[---,---,---]")
        return GameState(board)
