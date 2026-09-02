import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    data = np.array(data, dtype='float64')

    # filter out rows and get in row order
    data = data[row_start : row_stop, :]
    data = np.matrix.flatten(data)
    
    # remove 
    mask = (data > threshold)
    return data[mask]