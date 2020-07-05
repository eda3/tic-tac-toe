from board import Board
from gamestate import GameState
from setup_logger import setup_logger

logger = setup_logger(__name__)


def display_board(board: Board) -> str:
    """Boardをいい感じに出力"""
    sq: str = board.squares_string

    def get_sq(i: int) -> str:
        if sq[i] == "-":
            return " "
        else:
            return sq[i]

    text = (
        f"  1 2 3\n"
        f" ┏━┳━┳━┓\n"
        f"a┃{get_sq(0)}┃{get_sq(1)}┃{get_sq(2)}┃\n"
        f" ┣━╋━╋━┫\n"
        f"b┃{get_sq(3)}┃{get_sq(4)}┃{get_sq(5)}┃\n"
        f" ┣━╋━╋━┫\n"
        f"c┃{get_sq(6)}┃{get_sq(7)}┃{get_sq(8)}┃\n"
        f" ┗━┻━┻━┛\n"
    )
    return text


def main() -> None:
    game_state: GameState = GameState.initial()
    print(display_board(game_state.board))


if __name__ == "__main__":
    main()
