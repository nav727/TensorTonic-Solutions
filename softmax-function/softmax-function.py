import numpy as np


def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    
    x = np.array(x)

    # when input 2D, then all operations are row wise
    axis = 1 if (x.ndim > 1) else 0

    # subtract max for overflow issue
    x = x - np.max(x, axis=axis, keepdims=True)
    
    return np.exp(x) / np.sum(np.exp(x), axis=axis, keepdims=True)
  