import pytest
from board import Board
from gamestate import GameState


def test_initial():
    gs = GameState.initial()
    assert gs.board.to_notation() == "[123,456,789]"
