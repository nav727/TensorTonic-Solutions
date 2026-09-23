import numpy as np

def pairwise_diff(a: list) -> np.ndarray:
    """
    Returns an (n, n) float64 array of signed pairwise differences.
    """
    
    a = np.array(a, dtype='float64')
    ans = []
    for ele in a:
        ans.append(ele - a)

    return np.array(ans,dtype='float64')