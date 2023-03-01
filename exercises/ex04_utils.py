"""list Utility Functions"""
___author___: 730466273

def all(a: list[int], b: int) -> bool:
    """all"""
    j: int = 0
    while j < len(a):
        if a[j] == b:
            j = j + 1
        else:
            return False
    return True

def max(c: list[int]) -> int:
    """max"""
    d: int = 0 
    e: int = c[0]
    if len(c) == 0:
        raise ValueError("max() arg is an empty List")
    while d < len(c):
        if c[d] > e:
            e = c[d]
            d = d + 1
        else:
            d = d + 1
    return e

def is_equal(y: list[int], z: list[int]) -> bool:
    """is_equal"""
    if y == z:
        return True
    else:
        return False