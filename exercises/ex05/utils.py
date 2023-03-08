"""utils."""
__author__ = "730466273"

def only_evens(integers: list[int]) -> list[int]:
    """Only even numbers."""
    k: int = 0
    evens: list[int] = []
    while k < len(integers):
        if integers[k] % 2 == 0:
            evens.append(integers[k])
        k = k + 1
    return evens

def sub(main_set: list[int], start: int, end: int) -> list[int]:
    """Function between two indices."""
    subset: list[int] = list()
    if len(main_set) == 0: 
        return subset
    if start >= len(main_set):
        return subset
    if end <= 0:
        return subset
    
    if start < 0:
        start = 0
    if end > len(main_set):
        end = len(main_set)

    while start < end: 
        subset.append(main_set[start])
        start = start + 1
    return subset

def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Two lists of ints."""
    combined: list[int] = list()
    p: int = 0
    combined = list1
    while p < len(list2):
        combined.append(list2[p])
        p = p + 1
    return combined