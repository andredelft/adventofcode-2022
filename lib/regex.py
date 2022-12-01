import re


def parse_number(string: str) -> int | None:
    """Searches for first occurence of a number in a given string, and returns it as an integer if found, and None otherwise."""
    n = re.search(r"\d+", string)
    return int(n.group()) if n else None
