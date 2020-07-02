import pytest
from fillaction import FillAction


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
