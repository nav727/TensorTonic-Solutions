import numpy as np


def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    
    data = np.array(data, dtype='float64')
    
    max_val = np.max(data, axis = 1)
    max_col = np.argmax(data, axis=1)
    min_val = np.min(data, axis = 1)
    min_col = np.argmin(data, axis=1)

    combined = np.stack([max_val, max_col, min_val, min_col])

    return combined
    