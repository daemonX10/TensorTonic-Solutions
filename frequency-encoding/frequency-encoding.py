def frequency_encoding(values: list) -> list:
    """
    Returns the relative frequency of every input value.
    """
    # Write code here
    n = len(values)
    count = {}
    for v in values:
        count[v] = count.get(v,0)+1
    return [count[v]/n for v in values]