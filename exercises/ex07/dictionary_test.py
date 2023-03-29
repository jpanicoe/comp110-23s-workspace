"""EX07 Dictionary Function Test."""
__author__ = "7304662773"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest


def emptydict() -> None:
    """Edge Case."""
    dict_ie: dict[str, str] = {}
    assert invert(dict_ie) == {}


def testnormal() -> None: 
    """Normal."""
    dict_ie: dict[str, str] = {'kris': 'jordan', 'jack': 'panicoe'}
    assert invert(dict_ie) == {'panicoe': 'jack', 'jordan': 'michael'}


def testrepeat() -> None:
    """Repeat Keys."""
    my_dictionary: dict[str, str] = {}
    with pytest.raises(KeyError):
        my_dictionary = {"jordan": "kris", "jordan": "michael"}
        invert(my_dictionary)


def testmode2() -> None: 
    """Modes."""
    list_ie: list[str] = {"he", "him", "her", "she", "us"}
    assert count(list_ie) == {"he": 2, "him": 2, "her": 1}


def testempty() -> None: 
    """Empty."""
    list_ie: list[str] = []
    assert count(list_ie) == ()


def testlistnormal() -> None:
    """Normal."""
    list_ie: list[str] = {"he", "him", "her", "we"}
    assert count(list_ie) == {"he": 1, "him": 1, "her": 1, "we": 1}


def testmode1() -> None:
    """Multiple Modes."""
    dict_ie: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(dict_ie) == "blue"


def testnone() -> None: 
    """No Mode."""
    dict_ie: dict[str, str] = {"Marc": "green", "Ezri": "yellow", "Kris": "red"}
    assert favorite_color(dict_ie) == "green"


def testemptydict() -> None: 
    """Edge Case."""
    dict_ie: dict[str, str] = {}
    assert favorite_color(dict_ie) == ""