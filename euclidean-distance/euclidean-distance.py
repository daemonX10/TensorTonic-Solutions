import numpy as np
import math

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    n =len(x)
    ans = 0
    for i in range(n):
        ans+=(x[i]-y[i])**2
    return math.sqrt(ans)