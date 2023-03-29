"""EX07 Dictionary Functions."""
__author__ = "730466273"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Invert Dictionary."""
    dict2: dict[str, str] = {}
    if dict1 == {}:
        return {}
    for key in dict1:
        dict2[dict1[key]] = key
    repeat: dict[str, int] = {}
    repeat = count(dict1.values())
    if max(list(repeat.values())) > 1:
        raise KeyError("Repeated Keys Present")
    return dict2


def favoritecolor(colors: dict[str, str]) -> str:
    """Favorite Color."""
    if colors == {}: 
        return ""
    color = count(list(colors.values()))
    keys = list(color.keys())
    values = list(color.keys())
    index = values.index(max(values))
    return keys[index]


def count(list1: list[str]) -> dict[str, int]:
    """Counts Value in Input List."""
    dict_result: dict[str, int] = {}
    for key in list1:
        if key in dict_result:
            dict_result[key] += 1
        else:
            dict_result[key] = 1
        return dict_result