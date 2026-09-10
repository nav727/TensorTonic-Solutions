import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    
    data = np.array(data, dtype='float64')
    
    rnd = np.round(data, decimals)
    cel = np.ceil(data)
    flr = np.floor(data)

    # pad all the results
    rnd = np.pad(rnd, pad_width=pad_width)
    cel = np.pad(cel, pad_width=pad_width)
    flr = np.pad(flr, pad_width=pad_width)
    
    return np.stack([rnd, flr, cel])