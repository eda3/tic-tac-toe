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

    # ユーザアクションを取得
    input_action: str = input()

    # "quit"入力で修了
    while input_action != "quit":
        # 盤面記法が書かれたらゲームの状態を指定通りにリセット
        if Board.is_valid_notation(input_action):
            # 入力アクションを元にゲーム状態を生成
            board = Board.from_notation(input_action)
            game_state = GameState(board)

            # コンソールに盤面出力
            print(display_board(game_state.board))
            input_action = input()
        else:
            print("正しい値を入力してください")
            input_action = input()


if __name__ == "__main__":
    main()
