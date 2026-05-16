import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x = np.array(x)
    return np.percentile(x,q)
    