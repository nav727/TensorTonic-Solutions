import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    
    data = np.array(data, dtype='float64')
    col_mean = np.mean(data, axis=0)
    col_std = np.std(data, axis=0)
    
    return (data - col_mean) / col_std