import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x,dtype = float)
    p = np.array(p,dtype = float)
    if not np.allclose(np.sum(p),1) or np.size(x)!=np.size(p):
        raise ValueError("value don't addup to 1")
    
    return np.sum(x*p)
    
