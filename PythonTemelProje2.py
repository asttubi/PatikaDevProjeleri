def recursive_reversed(items):
    if isinstance(items, list):
        return [recursive_reversed(item) for item in reversed(items)]
    return items

recursive_reversed([[1, 2], [3, 4], [5, 6, 7]])