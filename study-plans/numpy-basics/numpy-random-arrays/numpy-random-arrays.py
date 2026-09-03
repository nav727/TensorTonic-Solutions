import numpy as np


def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    
    rng = np.random.default_rng(seed)
    
    if kind == 'uniform':
        return rng.uniform(low=0, high=1, size=shape)
        
    elif kind == 'normal':
        return rng.normal(loc=0, scale=1, size=shape)

