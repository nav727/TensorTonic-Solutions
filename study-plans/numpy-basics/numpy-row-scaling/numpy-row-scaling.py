import numpy as np

def scale_rows(data, weights):
    """Returns: np.ndarray of shape (m, n), each row scaled by corresponding weight"""
    
    data = np.array(data, dtype='float64')
    weights = np.array(weights, dtype='float64')

    # (m, n) X (m,)
    return (data.T * weights.reshape(1, -1)).T
    