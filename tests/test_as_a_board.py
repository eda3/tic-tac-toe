import pytest
import as_a_board
from board import Board
from gamestate import GameState


def test_display_board():
    game_state: GameState = GameState.initial()
    return_text: str = as_a_board.display_board(game_state.board)
    initial_text: str = (
        "  1 2 3\n"
        " ┏━┳━┳━┓\n"
        "a┃ ┃ ┃ ┃\n"
        " ┣━╋━╋━┫\n"
        "b┃ ┃ ┃ ┃\n"
        " ┣━╋━╋━┫\n"
        "c┃ ┃ ┃ ┃\n"
        " ┗━┻━┻━┛\n"
    )

    assert return_text == initial_text
