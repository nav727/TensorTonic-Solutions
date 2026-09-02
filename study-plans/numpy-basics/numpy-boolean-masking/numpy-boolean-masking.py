import numpy as np


def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    
    data = np.array(data, dtype='float64')

    # filter mask
    mask = (data > threshold).astype('int64')

    # keep row i unchanged if any element exceeds the threshold, else fill with 0.0
    any_mask = np.any(mask, axis=1, keepdims=True)
    any = np.where(any_mask, data, 0)
    
    # keep row i unchanged only if every element exceeds the threshold, else fill with 0.0
    all_mask = np.all(mask, axis=1, keepdims=True)
    all = np.where(all_mask, data, 0)
    
    return np.stack((mask, any, all), axis=0, dtype='float64')