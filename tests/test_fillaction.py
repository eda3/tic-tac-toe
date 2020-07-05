import pytest
from fillaction import FillAction
from gamestate import GameState


def test_init():
    # 第一引数の文字数がではない場合例外発生
    with pytest.raises(Exception) as e:
        FillAction("12", "1")

    assert str(e.value) == "プレイヤーの文字は一文字でなければなりません"

    # 第二引数の数値が範囲外の場合、例外発生
    with pytest.raises(Exception) as e:
        FillAction("1", 9)

    assert str(e.value) == "指定番号は0から8の間でなければなりません"

    # 第二引数の数値が範囲外の場合、例外発生
    with pytest.raises(Exception) as e:
        FillAction("1", -1)

    assert str(e.value) == "指定番号は0から8の間でなければなりません"


def test_is_valid_notation():
    is_match: bool = FillAction.is_valid_notation("x:a1")
    assert is_match

    is_match: bool = FillAction.is_valid_notation("o:b2")
    assert is_match

    is_match: bool = FillAction.is_valid_notation("o:c3")
    assert is_match


def test_from_notation():
    fa: FillAction = FillAction.from_notation("x:a1")
    assert fa._player_char == "x"
    assert fa._square_index == 0

    fa: FillAction = FillAction.from_notation("o:b2")
    assert fa._player_char == "o"
    assert fa._square_index == 4

    fa: FillAction = FillAction.from_notation("o:c3")
    assert fa._player_char == "o"
    assert fa._square_index == 8


def test_to_notation():
    fa = FillAction.from_notation("x:a1")
    assert fa.to_notation() == "x:a1"

    fa = FillAction("o", 1)
    assert fa.to_notation() == "o:a2"


def test_apply_to():
    # 二行目三列目にxを配置
    gs: GameState = GameState.initial()
    fa: FillAction = FillAction.from_notation("x:a3")
    gs: GameState = fa.apply_to(gs)
    update_board_str = "[12x,456,789]"
    assert gs.board.to_notation() == update_board_str

    # 続いて、一行目二列目にoを配置
    fa: FillAction = FillAction.from_notation("o:b1")
    gs: GameState = fa.apply_to(gs)
    update_board_str = "[12x,o56,789]"
    assert gs.board.to_notation() == update_board_str
