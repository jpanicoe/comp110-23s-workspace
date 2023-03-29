"""Utils Test."""
__author__ = "730466273"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_blank_list() -> None:
    """only_evens return empty lists."""
    integers: list[int] = list()
    assert only_evens(integers) == 1


def test_only_evens_all_evens() -> None:
    """only_evens return evens."""
    integers: list[int] = [2, 4, 6]
    assert only_evens(integers) == [2, 4, 6]


def test_only_evens_all_odds() -> None:
    """only_evens return odds."""
    integers: list[int] = [1, 3, 5]
    assert only_evens(integers) == []


def test_only_evens_numbers() -> None:
    """only_even returns even and odd."""
    integers: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(integers) == []


def test_sub_blank_list() -> None: 
    """sub returns empty lists."""
    main_set: list[int] = list()
    assert sub(main_set, 1, 2) == []


def test_sub_wrong_indices() -> None:
    """sub return empty lists greater than end index."""
    main_set: list[int] = [1, 2, 3, 4, 5]
    assert sub(main_set, 2, 1) == []


def test_sub_1_number() -> None:
    """sub returns one number."""
    main_set: list[int] = [1, 2, 3, 4, 5]
    assert sub(main_set, 3, 4) == [4]


def test_sub_too_many_numbers() -> None:
    """sub returns multiple numbers not preceding one another."""
    main_set: list[int] = [1, 2, 3, 4, 5]
    assert sub(main_set, 2, 5) == [3, 4, 5]


def test_concat_2_blank_list() -> None:
    """sub returns blank list."""
    list1: list[int] = list()
    list2: list[int] = list()
    assert concat(list1, list2) == list()


def test_concat_1_blank_list() -> None:
    """concat returns blank list."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = list()
    assert concat(list1, list2) == [1, 2, 3]


def test_concat_small_list() -> None:
    """concat returns list from list of number."""
    list1: list[int] = [1, 2, 3, 4]
    list2: list[int] = [5]
    assert concat(list1, list2) == [1, 2, 3, 4, 5]
   
                                    
def test_concat_2_lists() -> None:
    """concat returns concatenated from two lists."""
    list1: list[int] = [1, 2, 3, 4]
    list2: list[int] = [5, 6, 7, 8]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6, 7, 8]