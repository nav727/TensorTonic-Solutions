import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    
    data = np.array(data, dtype='float64')

    sorted_data = np.sort(data, axis=axis)
    idx_order = np.argsort(data, axis=axis)
    
    combined = np.stack([sorted_data, idx_order])
    return combined