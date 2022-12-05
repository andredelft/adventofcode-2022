def split_list(obj: list, index: int) -> tuple[list, list]:
    """Splits list into two at given index."""
    return obj[:index], obj[index:]
