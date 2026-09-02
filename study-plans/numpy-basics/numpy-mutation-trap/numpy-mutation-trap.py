import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    
    data = np.array(data, dtype='float64')

    ori = data[row_idx, :]
    clipped = np.clip(ori, a_min=lo, a_max=hi)
    
    return np.stack([ori, clipped], axis=0, dtype='float64')