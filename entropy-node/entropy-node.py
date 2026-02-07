import numpy as np
from collections import defaultdict 

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    mapp = defaultdict(int)
    for i in y:
        mapp[i]+=1
    
    n = len(y)
    entropy=0.0
    for _,val in mapp.items():
        prob = val/n
        entropy -= (prob * np.log2(prob))
    
    return entropy
