from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    
    x = np.array(x)
    distinct_nums, counts = np.unique(x, return_counts=True)
    mode = distinct_nums[np.argmax(counts)]
    
    return {'mean'  : float(np.mean(x)),
           'median' : float(np.median(x)),
           'mode'   : float(mode)}