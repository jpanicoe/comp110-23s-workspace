"""EX07 Dictionary Function Test."""
__author__ = "7304662773"


import pytest
from dictionary import invert
from dictionary import favoritecolor
from dictionary import count


def emptydict() -> None:
    """Edge Case."""
    dictie: dict[str, str] = {}
    assert invert(dictie) == {}


def testnormal() -> None: 
    """Normal."""
    dictie: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(dictie) == {'jordan': 'kris', 'jordan': 'michael'}


def testrepeat() -> None:
    """Repeat Keys."""
    my_dictionary: dict[str, str] = {}
    with pytest.raises(KeyError):
        my_dictionary = {"jordan": "kris", "jordan": "michael"}
        invert(my_dictionary)


def testmode2() -> None: 
    """Modes."""
    listie: list[str] = {"he", "him", "she", "he", "him"}
    assert count(listie) == {"he": 2, "him": 2, "she": 1}


def testempty() -> None: 
    """Empty."""
    listie: list[str] = []
    assert count(listie) == ()


def testlistnormal() -> None:
    """Normal."""
    listie: list[str] = {"he", "him", "she", "her"}
    assert count(listie) == {"he": 1, "him": 1, "she": 1, "her": 1}


def testmode1() -> None:
    """Multiple Modes."""
    dictie: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favoritecolor(dictie) == "blue"


def testnone() -> None: 
    """No Mode."""
    dictie: dict[str, str] = {"Marc": "green", "Ezri": "red", "Kris": "blue"}
    assert favoritecolor(dictie == "green")


def testemptydict() -> None: 
    """Edge Case."""
    dictie: dict[str, str] = {}
    assert favoritecolor(dictie) == ""