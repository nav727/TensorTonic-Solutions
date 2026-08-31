import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # use np only
    x = np.array(x)
    p = np.array(p)
    
    return np.float64(np.sum(x * p))