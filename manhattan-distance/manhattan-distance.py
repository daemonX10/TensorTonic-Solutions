import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x = np.array(x,dtype=float)
    y = np.array(y,dtype = float)
    ans = np.sum(np.abs(x-y),dtype=float)
    return ans