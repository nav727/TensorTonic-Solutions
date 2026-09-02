import numpy as np

def create_sequence(start, stop, param, kind):
    """
    Returns: 1D ndarray of float64 values
    """
    
    if kind == 'arange':
        # will not include the stop and be a step size
        return np.arange(start, stop, param, dtype='float64')
        
    elif kind == 'linspace':
        # will include the stop and divide equally
        return np.linspace(start, stop, param, dtype='float64')
