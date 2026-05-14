import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    arr = np.asarray(x)
    n = arr.size
    if n<2:
        raise ValueError("X must contain at least two values")
    mean = np.mean(arr)
    s2 =  np.sum((arr-mean)**2)/(n-1)
    s = np.sqrt(s2)
    return float(s2),float(s)