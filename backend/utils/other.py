def merge_values(value1, value2):
    if value1 is None and value2 is None:
        return None

    if value1 is None:
        return value2

    if value2 is None:
        return value1

    if isinstance(value1, list):
        set_result = set(value1)
    else:
        set_result = {value1}

    set_result.add(value2)

    if len(set_result) == 1:
        return set_result.pop()
    else:
        return list(set_result)
