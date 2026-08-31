import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    x = np.asarray(x, dtype=float)
    result = np.where(
        x >= 0,
        1 / (1 + np.exp(-x)),          # safe for large positive x
        np.exp(x) / (1 + np.exp(x))    # safe for large negative x
    )
    return result