import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    ans = 0
    n = len(x)
    for i in range(n):
        ans+=abs(x[i]-y[i])
    return float(ans)